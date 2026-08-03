"""
behavioral_interview_guide.py

Generates a complete Behavioral Interview Guide.

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator
from modules.logger import get_logger

logger = get_logger(__name__)


class BehavioralInterviewGuide(BaseAIGenerator):
    """
    Generates a complete behavioral interview preparation guide.
    """

    OUTPUT_FILE = "behavioral_interview_guide.md"
    LOG_NAME = "Behavioral Interview Guide"

    SECTIONS = [
        (
            "behavioral/behavioral_prompt.txt",
            "Behavioral Questions",
        ),
        (
            "behavioral/hr_prompt.txt",
            "HR Questions",
        ),
        (
            "behavioral/company_prompt.txt",
            "Company Research",
        ),
        (
            "behavioral/questions_to_ask_prompt.txt",
            "Questions To Ask Interviewer",
        ),
        (
            "behavioral/checklist_prompt.txt",
            "Interview Checklist",
        ),
    ]

    def generate(self, context: dict) -> str:
        """
        Generate the complete behavioral interview guide.
        """

        report = ""

        for template_name, title in self.SECTIONS:

            logger.info(f"Generating {title}...")

            report += f"# {title}\n\n"

            report += self.generate_content(
                template_name=template_name,
                prompt_values=context,
            )

            report += "\n\n"

        return self.save_document(
            content=report,
            output_filename=self.OUTPUT_FILE,
        )