"""
interview_preparation_guide.py

AI Interview Preparation Guide Generator

Responsibilities:
- Generate a complete interview preparation guide
- Save the guide as Markdown

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator


class InterviewPreparationGuide(BaseAIGenerator):
    """
    AI-powered Interview Preparation Guide Generator.
    """

    TEMPLATE_NAME = "interview/interview_preparation_guide_prompt.txt"

    OUTPUT_FILE = "interview_preparation_guide.md"

    LOG_NAME = "Interview Preparation Guide"

    def generate(
        self,
        resume_text: str,
        job_description: str,
        ats_report: str,
    ) -> str:
        """
        Generate a personalized interview preparation guide.
        """

        prompt_values = {
            "resume": resume_text,
            "job_description": job_description,
            "ats_report": ats_report,
        }

        return self.generate_document(
            prompt_values
        )