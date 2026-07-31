"""
cover_letter_generator.py

AI Cover Letter Generator

Responsibilities:
- Build cover letter prompt
- Send prompt to AI
- Save generated cover letter
- Return output file path

Author: Raju Nalla
"""

from pathlib import Path

from config.config_loader import ConfigLoader
from modules.ai_client import AIClient
from modules.logger import get_logger
from modules.prompt_builder import PromptBuilder

logger = get_logger(__name__)


class CoverLetterGenerator:
    """
    AI-powered Cover Letter Generator.
    """

    def __init__(self):

        config = ConfigLoader()

        self.prompt_builder = PromptBuilder(
            config.get("paths.prompts")
        )

        self.ai_client = AIClient()

        self.output_directory = Path(
            config.get("paths.reports")
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def generate(
        self,
        resume_text: str,
        job_description: str,
        candidate_name: str
    ) -> str:
        """
        Generate a personalized cover letter.
        """

        logger.info(
            "Generating cover letter prompt..."
        )

        prompt = self.prompt_builder.build_prompt(
            "cover_letter_prompt.txt",
            {
                "resume": resume_text,
                "job_description": job_description,
                "candidate_name": candidate_name,
            },
        )

        logger.info(
            "Sending cover letter prompt to AI model..."
        )

        cover_letter = self.ai_client.generate(
            prompt
        )

        output_file = (
            self.output_directory /
            "cover_letter.md"
        )

        output_file.write_text(
            cover_letter,
            encoding="utf-8"
        )

        logger.info(
            f"Cover letter saved to {output_file}"
        )

        return str(output_file)