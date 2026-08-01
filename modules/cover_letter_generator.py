"""
cover_letter_generator.py

AI Cover Letter Generator

Responsibilities:
- Generate personalized cover letter

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator


class CoverLetterGenerator(BaseAIGenerator):
    """
    AI-powered Cover Letter Generator.
    """

    TEMPLATE_NAME = "cover_letter/cover_letter_prompt.txt"

    OUTPUT_FILE = "cover_letter.md"

    LOG_NAME = "Cover Letter"

    def generate(
        self,
        resume_text: str,
        job_description: str,
        candidate_name: str,
    ) -> str:
        """
        Generate cover letter.
        """

        prompt_values = {
            "resume": resume_text,
            "job_description": job_description,
            "candidate_name": candidate_name,
        }

        return self.generate_document(
            prompt_values
        )