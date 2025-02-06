import re

def sanitize_query(query):
    """Sanitize the query to prevent command injection."""
    sanitized_query = re.sub(r'[\'\"`\\$]', '', query)
    return sanitized_query.strip()

import logging

def log_query_result(email_address, query, result_file):
    """Log the email address, query, and result file path."""
    try:
        log_entry = f"Email: {email_address}\nQuery: {query}\nResult: {result_file}\n\n"
        with open('query_results.log', 'a') as log_file:
            log_file.write(log_entry)
        logging.info("Logged query result.")
    except Exception as e:
        logging.error(f"Error logging query result: {e}")
