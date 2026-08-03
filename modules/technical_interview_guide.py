"""
technical_interview_guide.py

Generates the complete Technical Interview Guide.

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator
from modules.logger import get_logger

logger = get_logger(__name__)


class TechnicalInterviewGuide(BaseAIGenerator):

    OUTPUT_FILE = "technical_interview_guide.md"

    SECTIONS = [

        (
            "interview/beginner_prompt.txt",
            "Beginner Technical Questions",
        ),

        (
            "interview/intermediate_prompt.txt",
            "Intermediate Technical Questions",
        ),

        (
            "interview/advanced_prompt.txt",
            "Advanced Technical Questions",
        ),

        (
            "interview/scenario_prompt.txt",
            "Scenario-Based Questions",
        ),

        (
            "interview/top10_prompt.txt",
            "Top 10 Most Important Interview Questions",
        ),

    ]

    def generate(self, context: dict):

        report = "# Technical Interview Guide\n\n"

        for template_name, section_title in self.SECTIONS:

            logger.info(f"Generating {section_title}...")

            report += f"\n---\n\n# {section_title}\n\n"

            report += self.generate_content(
                template_name=template_name,
                prompt_values=context,
            )

            report += "\n\n"

        return self.save_document(
            content=report,
            output_filename=self.OUTPUT_FILE,
        )