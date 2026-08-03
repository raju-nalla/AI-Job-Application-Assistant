"""
cover_letter_generator.py

AI Cover Letter Generator

Responsibilities:
- Generate a personalized cover letter.

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

    def generate(self, context: dict) -> str:
        """
        Generate a personalized cover letter using the shared context.
        """

        return self.generate_document(
            template_name=self.TEMPLATE_NAME,
            prompt_values=context,
            output_file=self.OUTPUT_FILE,
        )