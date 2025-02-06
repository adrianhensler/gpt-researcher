import os
from dotenv import load_dotenv

load_dotenv()

# Email configuration
IMAP_SERVER = os.getenv('AITOOLS_IMAP_SERVER')
IMAP_PORT = int(os.getenv('AITOOLS_IMAP_PORT', 993))
SMTP_SERVER = os.getenv('AITOOLS_SMTP_SERVER')
SMTP_PORT = int(os.getenv('AITOOLS_SMTP_PORT', 587))
EMAIL_ACCOUNT = os.getenv('AITOOLS_EMAIL_ACCOUNT')
EMAIL_PASSWORD = os.getenv('AITOOLS_EMAIL_PASSWORD')

# Logging file path
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'detailed_report.log')
