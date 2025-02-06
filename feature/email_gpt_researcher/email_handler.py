import imaplib
import email
import logging
import asyncio
import os
import smtplib
import mimetypes

from email.message import EmailMessage

from aitool_gpt_researcher import config, utils, report_generator


def extract_email_body(msg):
    """
    Extracts the plain text body from an email message.

    Args:
        msg (email.message.Message): The email message object.

    Returns:
        str or None: The extracted plain text, or None if extraction fails.
    """
    try:
        if msg.is_multipart():
            for part in msg.walk():
                # Only consider plain text parts that aren't attachments.
                if part.get_content_type() == "text/plain" and not part.get('Content-Disposition'):
                    return part.get_payload(decode=True).decode('utf-8')
        else:
            return msg.get_payload(decode=True).decode('utf-8')
    except Exception as e:
        logging.error(f"Error extracting email body: {e}")
    return None


def send_email_with_attachment(to_email, subject, file_path, original_msg):
    """
    Sends an email reply with a PDF attachment.

    Args:
        to_email (str): Recipient email address.
        subject (str): Subject of the original email.
        file_path (str): Path to the PDF file.
        original_msg (email.message.Message): The original email message.
    """
    try:
        msg = EmailMessage()
        msg['Subject'] = f"Re: {subject}"
        msg['From'] = config.EMAIL_ACCOUNT
        msg['To'] = to_email
        msg['In-Reply-To'] = original_msg['Message-ID']
        msg['References'] = original_msg['Message-ID']

        body = f"""Dear {to_email},

Please find attached the detailed report you requested.

Best regards,
Your Automated Report Service
"""
        msg.set_content(body)

        # Attach the PDF file.
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)

        mime_type, _ = mimetypes.guess_type(file_name)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        maintype, subtype = mime_type.split('/')
        msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_ACCOUNT, config.EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")


def check_email():
    """
    Connects to the IMAP server, searches for unseen emails with "Detailed_Report" in the subject,
    processes each email to generate a report and reply, and then logs out.
    """
    mail = None
    try:
        logging.info("Connecting to IMAP server...")
        mail = imaplib.IMAP4_SSL(config.IMAP_SERVER, config.IMAP_PORT)
    except Exception as e:
        logging.error(f"Failed to connect to IMAP server: {e}")
        return

    try:
        try:
            mail.login(config.EMAIL_ACCOUNT, config.EMAIL_PASSWORD)
        except imaplib.IMAP4.error as e:
            logging.error(f"IMAP login failed: {e}")
            return

        try:
            mail.select('inbox')
        except Exception as e:
            logging.error(f"Error selecting inbox: {e}")
            return

        result, data = mail.search(None, '(UNSEEN SUBJECT "Detailed_Report")')
        if result != 'OK':
            logging.error("Failed to search for emails.")
            return

        email_ids = data[0].split()
        if not email_ids:
            logging.info("No new emails found.")
            return

        for email_id in email_ids:
            try:
                result, data = mail.fetch(email_id, '(BODY.PEEK[])')
                if result != 'OK':
                    logging.error(f"Failed to fetch email with id {email_id}")
                    continue

                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)
                from_email = email.utils.parseaddr(msg['From'])[1]
                subject = msg['Subject']
                email_body = extract_email_body(msg)

                if not email_body:
                    logging.error(f"No query found in the email from {from_email}")
                    continue

                query = email_body.strip()
                logging.info(f"Received query from {from_email}: {query}")

                # Sanitize the query.
                sanitized_query = utils.sanitize_query(query)

                try:
                    report_file = asyncio.run(report_generator.generate_report(sanitized_query))
                except Exception as e:
                    logging.error(f"Error generating report for {from_email}: {e}")
                    continue

                if report_file:
                    try:
                        send_email_with_attachment(from_email, subject, report_file, msg)
                        logging.info(f"Processed and replied to email from {from_email}")
                        # Use the log_query_result from utils.
                        utils.log_query_result(from_email, sanitized_query, report_file)
                        mail.store(email_id, '+FLAGS', '\\Seen')
                    except Exception as e:
                        logging.error(f"Error sending email with attachment for {from_email}: {e}")
                else:
                    logging.error(f"Failed to generate report for {from_email}")
            except Exception as e:
                logging.error(f"Error processing email with id {email_id}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in check_email: {e}")
    finally:
        if mail is not None:
            try:
                mail.logout()
                logging.info("Logged out from email server.")
            except Exception as e:
                logging.error(f"Error logging out from email server: {e}")
