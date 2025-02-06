import os
import time
import datetime
import logging
import markdown
from bs4 import BeautifulSoup
import pdfkit
from email_gpt_researcher.image_handler import cleanup_images

def create_pdf_report(report_output):
    """
    Create a PDF report from the given report_output dictionary.
    """
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = report_output.get("query", "Unknown Query")
        report = report_output.get("report", "No report generated.")
        sources = report_output.get("sources", [])
        include_sources = report_output.get("include_sources", False)

        # Convert Markdown to HTML
        report_html = markdown.markdown(report)
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Detailed Report</title>
            <style>
                /* Add CSS styles as needed */
                body {{ font-family: Arial, sans-serif; }}
                .header {{ text-align: center; margin-bottom: 20px; }}
                .section {{ margin: 20px; }}
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Detailed Report</h1>
                <p>Generated on {timestamp}</p>
            </div>
            <div class="section">
                <h2>Initial Prompt</h2>
                <p>{query}</p>
            </div>
            <div class="section">
                <h2>Report</h2>
                {report_html}
            </div>
        """
        if include_sources and sources:
            html_content += """
            <div class="section">
                <h2>Research Sources</h2>
                <table>
                    <tr><th>#</th><th>Source</th></tr>
            """
            for idx, source in enumerate(sources):
                html_content += f"<tr><td>{idx+1}</td><td>{source}</td></tr>"
            html_content += """
                </table>
            </div>
            """
        html_content += """
        </body>
        </html>
        """

        # Prettify HTML for consistency
        soup = BeautifulSoup(html_content, 'html.parser')
        prettified_html = soup.prettify()

        # Write HTML to a temporary file
        html_file = f"report_{int(time.time())}.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(prettified_html)

        # Convert HTML to PDF using pdfkit options
        pdf_file = f"{os.path.splitext(html_file)[0]}.pdf"
        options = {
            "enable-local-file-access": "",
            "disable-smart-shrinking": "",
            "no-stop-slow-scripts": "",
        }
        pdfkit.from_file(html_file, pdf_file, options=options)

        # Remove the temporary HTML file and cleanup images
        os.remove(html_file)
        cleanup_images()

        if os.path.isfile(pdf_file):
            logging.info(f"PDF generated at: {pdf_file}")
            return pdf_file
        else:
            logging.error("PDF file not found after conversion.")
            return None
    except Exception as e:
        logging.error(f"Error creating PDF report: {e}")
        return None
