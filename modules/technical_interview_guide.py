"""
technical_interview_guide.py

Generates a Technical Interview Guide.

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator


class TechnicalInterviewGuide(BaseAIGenerator):
    """
    Generates technical interview preparation questions.
    """

    TEMPLATE_NAME = "interview/technical_interview_prompt.txt"

    OUTPUT_FILE = "technical_interview_guide.md"

    LOG_NAME = "Technical Interview Guide"

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