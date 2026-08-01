"""
interview_overview.py

Generates a personalized Interview Overview.

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator


class InterviewOverview(BaseAIGenerator):
    """
    Generates a concise interview overview.
    """

    TEMPLATE_NAME = "interview/interview_overview_prompt.txt"

    OUTPUT_FILE = "interview_overview.md"

    LOG_NAME = "Interview Overview"

    def generate(
        self,
        resume_text: str,
        job_description: str,
        ats_report: str,
    ) -> str:

        prompt_values = {
            "resume": resume_text,
            "job_description": job_description,
            "ats_report": ats_report,
        }

        return self.generate_document(prompt_values)