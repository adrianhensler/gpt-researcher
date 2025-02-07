## Needs review; I've had to change things to make it "presentable" which involved some changes; any breakage here is likely due to path issues.

# Email GPT Researcher

An email-based interface for GPT Researcher that automatically processes research requests and returns detailed PDF reports.

Please note this document was generated mostly by AI; as was the code. Any corrections welcome.

## Overview

Email GPT Researcher is an optional extension for the GPT Researcher project that enables users to submit research queries via email and receive comprehensive PDF reports in response. The system monitors a designated email inbox for messages with "detailed_report" (not case sensitive) in the subject line, processes the research requests using GPT Researcher, and sends back professionally formatted PDF reports.

## Features

- **Email-Based Interface**: Automatically monitors and processes research requests received via email
- **Automated Report Generation**: Leverages GPT Researcher to create detailed reports on requested topics
- **PDF Report Creation**: Generates professional PDF reports with proper formatting and source citations
- **Asynchronous Processing**: Handles multiple research requests concurrently
- **Logging System**: Maintains detailed logs of all requests and operations

## Prerequisites

- Python 3.8+
- GPT Researcher installed and configured
- Email account with IMAP/SMTP access
- wkhtmltopdf installed for PDF generation

## Installation

1. Clone this repository into your GPT Researcher project:
```bash
cd gpt-researcher
git clone [repository-url] feature/email_gpt_researcher
```

2. Install required dependencies:
```bash
pip install python-dotenv beautifulsoup4 markdown pdfkit imaplib-status
```

3. Install wkhtmltopdf:
- On Ubuntu/Debian: `sudo apt-get install wkhtmltopdf`
- On macOS: `brew install wkhtmltopdf`
- On Windows: Download from the official website

## Configuration

1. Create a `.env` file in your project root with the following variables:
```env
AITOOLS_IMAP_SERVER=imap.example.com
AITOOLS_IMAP_PORT=993
AITOOLS_SMTP_SERVER=smtp.example.com
AITOOLS_SMTP_PORT=587
AITOOLS_EMAIL_ACCOUNT=your-email@example.com
AITOOLS_EMAIL_PASSWORD=your-password
```

2. Ensure the email account has IMAP enabled and appropriate app passwords configured if using 2FA.

## Usage

1. Start the email monitor:
```bash
python -m feature.email_gpt_researcher.main
```

2. Send an email with:
   - Subject containing "detailed_report" (not case-sensitive)
   - Body containing your research query  ## TODO better stripping of forced footers etc in email (legalese, OOO etc? Optional API call?)

3. The system will:
   - Process your request using GPT Researcher
   - Generate a detailed PDF report
   - Reply to your email with the report attached

## Security Considerations

- Use environment variables for sensitive credentials
- Enable SSL/TLS for email connections
- Consider implementing rate limiting
- Regularly monitor logs for suspicious activity
- Use application-specific passwords when possible
- Keep all dependencies updated

## Logging

The system maintains two types of logs:
- `detailed_report.log`: System operations and errors
- `query_results.log`: Track of processed queries and results

Logs are stored in the feature directory by default.

## Known Limitations

- Currently only processes plain text email bodies
- No support for attachments in incoming emails
- Limited to one research query per email

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Future Improvements

- [ ] Add support for multiple queries per email
- [ ] Implement rate limiting
- [ ] Add email templates customization
- [ ] Support for different report formats
- [ ] Add query validation and sanitization
- [ ] Implement retry mechanism for failed operations
- [ ] Add support for attachment processing

## License

[Specify your license here]

## Acknowledgments

- Based on the [GPT Researcher](https://github.com/assafelovic/gpt-researcher) project
- Uses various open-source libraries

## Results from quick review of code via Claude / Anthropic:

I'll review the code first and then create a README.md file. Let me analyze potential issues:

Critical Issues:
1. Email Security:
   - The code uses IMAP's `BODY.PEEK[]` which downloads the entire email, potentially exposing sensitive data
   - No size limits on email attachments or bodies, could lead to memory issues
   - No rate limiting on incoming emails, potential for DoS
   - Stores email credentials in .env without specifying required encryption

2. Input Validation:
   - Basic sanitization only removes a few special characters
   - No validation of email addresses or subject lines
   - No maximum length checks on queries

3. Resource Management:
   - No timeout on report generation
   - No limit on concurrent processing
   - Image files are stored locally without size limits
   - Temporary files might not be cleaned up if process crashes

4. Error Handling:
   - Some error paths may leave IMAP connection open
   - PDF generation errors might leave temporary HTML files
   - No retry mechanism for failed email sends

Let me create a comprehensive README.md for this project:





# Email GPT Researcher

An email-based interface for GPT Researcher that automatically processes research requests and returns detailed PDF reports.

## Overview

Email GPT Researcher is an extension for the GPT Researcher project that enables users to submit research queries via email and receive comprehensive PDF reports in response. The system monitors a designated email inbox for messages with "Detailed_Report" in the subject line, processes the research requests using GPT Researcher, and sends back professionally formatted PDF reports.

## Features

- **Email-Based Interface**: Automatically monitors and processes research requests received via email
- **Automated Report Generation**: Leverages GPT Researcher to create detailed reports on requested topics
- **PDF Report Creation**: Generates professional PDF reports with proper formatting and source citations
- **Asynchronous Processing**: Handles multiple research requests concurrently
- **Logging System**: Maintains detailed logs of all requests and operations

## Prerequisites

- Python 3.8+
- GPT Researcher installed and configured
- Email account with IMAP/SMTP access
- wkhtmltopdf installed for PDF generation

## Installation

1. Clone this repository into your GPT Researcher project:
```bash
cd gpt-researcher
git clone [repository-url] feature/email_gpt_researcher
```

2. Install required dependencies:
```bash
pip install python-dotenv beautifulsoup4 markdown pdfkit imaplib-status
```

3. Install wkhtmltopdf:
- On Ubuntu/Debian: `sudo apt-get install wkhtmltopdf`
- On macOS: `brew install wkhtmltopdf`
- On Windows: Download from the official website

## Configuration

1. Create a `.env` file in your project root with the following variables:
```env
AITOOLS_IMAP_SERVER=imap.example.com
AITOOLS_IMAP_PORT=993
AITOOLS_SMTP_SERVER=smtp.example.com
AITOOLS_SMTP_PORT=587
AITOOLS_EMAIL_ACCOUNT=your-email@example.com
AITOOLS_EMAIL_PASSWORD=your-password
```

2. Ensure the email account has IMAP enabled and appropriate app passwords configured if using 2FA.

## Usage

1. Start the email monitor:
```bash
python -m feature.email_gpt_researcher.main
```

2. Send an email with:
   - Subject containing "Detailed_Report"
   - Body containing your research query

3. The system will:
   - Process your request using GPT Researcher
   - Generate a detailed PDF report
   - Reply to your email with the report attached

## Security Considerations

- Use environment variables for sensitive credentials
- Enable SSL/TLS for email connections
- Consider implementing rate limiting
- Regularly monitor logs for suspicious activity
- Use application-specific passwords when possible
- Keep all dependencies updated

## Logging

The system maintains two types of logs:
- `detailed_report.log`: System operations and errors
- `query_results.log`: Track of processed queries and results

Logs are stored in the feature directory by default.

## Known Limitations

- Currently only processes plain text email bodies
- No support for attachments in incoming emails
- Limited to one research query per email
- Subject must contain exact phrase "Detailed_Report"

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Future Improvements

- [ ] Add support for multiple queries per email
- [ ] Implement rate limiting
- [ ] Add email templates customization
- [ ] Support for different report formats
- [ ] Add query validation and sanitization
- [ ] Implement retry mechanism for failed operations
- [ ] Add support for attachment processing

## License

TBD

## Acknowledgments

- Based on the [GPT Researcher](https://github.com/assafelovic/gpt-researcher) project
- Uses various open-source libraries

## Review of the code via Clause / Anthropic:

To improve the code's security and reliability, I recommend implementing these changes:

1. Add input validation:
```python
def validate_email_size(email_body):
    MAX_SIZE = 1024 * 1024  # 1MB
    return len(email_body) <= MAX_SIZE

def validate_query(query):
    MAX_QUERY_LENGTH = 1000
    return len(query) <= MAX_QUERY_LENGTH
```

2. Implement rate limiting:
```python
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
        self.MAX_REQUESTS = 10
        self.TIME_WINDOW = 3600  # 1 hour

    def is_rate_limited(self, email):
        now = time.time()
        self.requests[email] = [t for t in self.requests[email] if now - t < self.TIME_WINDOW]
        if len(self.requests[email]) >= self.MAX_REQUESTS:
            return True
        self.requests[email].append(now)
        return False
```

3. Add proper resource cleanup:
```python
def cleanup_resources(temp_files):
    for file in temp_files:
        try:
            if os.path.exists(file):
                os.remove(file)
        except Exception as e:
            logging.error(f"Failed to cleanup {file}: {e}")
```

4. Implement better error handling and retries:
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def send_email_with_retry(to_email, subject, file_path, original_msg):
    # Existing send_email_with_attachment code here
```

## Configuration example

You'll need the .env variables as detailed above. I trigger it via crontab:

Crontab entry such as:

```
*/15 * * * * /home/automate/automate/cron_run_gptr.sh >> /home/automate/automate/logs//cron_tts_gptr_email.log 2>&1
```

The above calls cron_run_gptr.sh:

cron_run_gptr.sh:

```
#!/bin/bash
# Activate the virtual environment
source /home/automate/code/gptresearcher/gpt-researcher/env/bin/activate
# Run the Python script
# python /home/automate/code/gptresearcher/gpt-researcher/feature/email_gpt_researcher.py
cd /home/automate/code/gptresearcher/gpt-researcher/feature
python -m email_gpt_researcher.main
# Now run other python script to deactivate
deactivate
```

