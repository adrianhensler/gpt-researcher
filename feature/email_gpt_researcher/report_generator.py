import asyncio
import logging
from backend.report_type.detailed_report.detailed_report import DetailedReport
from feature.email_gpt_researcher import pdf_generator

async def generate_report(query):
    """
    Generate a detailed research report and return the path to the generated PDF.
    """
    try:
        researcher = DetailedReport(
            query=query,
            report_type="detailed_report",
            report_source="web",
            tone="Objective"
        )
        # Run the research asynchronously
        report_text = await researcher.run()

        # Wrap the output in a dictionary
        report_output = {
            "query": query,
            "report": report_text,
            "context": {},
            "costs": {},
            "images": [],
            "sources": []
        }
        return pdf_generator.create_pdf_report(report_output)
    except Exception as e:
        logging.error(f"Error generating detailed report: {e}")
        return None
