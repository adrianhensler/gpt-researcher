Email GPT Researcher
An email-based interface for GPT Researcher that automatically processes research requests and returns detailed PDF reports.
Overview
Email GPT Researcher is an extension for the GPT Researcher project that enables users to submit research queries via email and receive comprehensive PDF reports in response. The system monitors a designated email inbox for messages with "Detailed_Report" in the subject line, processes the research requests using GPT Researcher, and sends back professionally formatted PDF reports.
Features

Email-Based Interface: Automatically monitors and processes research requests received via email
Automated Report Generation: Leverages GPT Researcher to create detailed reports on requested topics
PDF Report Creation: Generates professional PDF reports with proper formatting and source citations
Asynchronous Processing: Handles multiple research requests concurrently
Logging System: Maintains detailed logs of all requests and operations

Prerequisites

Python 3.8+
GPT Researcher installed and configured
Email account with IMAP/SMTP access
wkhtmltopdf installed for PDF generation

Installation

Clone this repository into your GPT Researcher project:

bashCopycd gpt-researcher
git clone [repository-url] feature/email_gpt_researcher

Install required dependencies:

bashCopypip install python-dotenv beautifulsoup4 markdown pdfkit imaplib-status

Install wkhtmltopdf:


On Ubuntu/Debian: sudo apt-get install wkhtmltopdf
On macOS: brew install wkhtmltopdf
On Windows: Download from the official website

Configuration

Create a .env file in your project root with the following variables:

envCopyAITOOLS_IMAP_SERVER=imap.example.com
AITOOLS_IMAP_PORT=993
AITOOLS_SMTP_SERVER=smtp.example.com
AITOOLS_SMTP_PORT=587
AITOOLS_EMAIL_ACCOUNT=your-email@example.com
AITOOLS_EMAIL_PASSWORD=your-password

Ensure the email account has IMAP enabled and appropriate app passwords configured if using 2FA.

Usage

Start the email monitor:

bashCopypython -m feature.email_gpt_researcher.main

Send an email with:

Subject containing "Detailed_Report"
Body containing your research query


The system will:

Process your request using GPT Researcher
Generate a detailed PDF report
Reply to your email with the report attached



Security Considerations

Use environment variables for sensitive credentials
Enable SSL/TLS for email connections
Consider implementing rate limiting
Regularly monitor logs for suspicious activity
Use application-specific passwords when possible
Keep all dependencies updated

Logging
The system maintains two types of logs:

detailed_report.log: System operations and errors
query_results.log: Track of processed queries and results

Logs are stored in the feature directory by default.
Known Limitations

Currently only processes plain text email bodies
No support for attachments in incoming emails
Limited to one research query per email
Subject must contain exact phrase "Detailed_Report"

Contributing
Contributions are welcome! Please:

Fork the repository
Create a feature branch
Submit a pull request

Future Improvements

 Add support for multiple queries per email
 Implement rate limiting
 Add email templates customization
 Support for different report formats
 Add query validation and sanitization
 Implement retry mechanism for failed operations
 Add possible support for attachment processing (worth dumping attachments to vectordb? Web likely better)

Thanks to GPT-Researcher project
Uses various open-source libraries
