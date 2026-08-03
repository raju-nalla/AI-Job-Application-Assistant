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

    def generate(self, context: dict) -> str:
        """
        Generate interview overview using the shared context.
        """

        return self.generate_document(
            template_name=self.TEMPLATE_NAME,
            prompt_values=context,
            output_file=self.OUTPUT_FILE,
        )