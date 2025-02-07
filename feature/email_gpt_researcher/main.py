import argparse
import logging
import os
from feature.email_gpt_researcher import config, email_handler

# Configure logging (here we use the log file path from config)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

def main():
    parser = argparse.ArgumentParser(description="Process emails and generate detailed reports.")
    args = parser.parse_args()
    email_handler.check_email()
    logging.info("Email check completed.")

if __name__ == "__main__":
    main()
