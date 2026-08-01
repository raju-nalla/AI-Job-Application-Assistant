"""
base_ai_generator.py

Base class for all AI-powered generators.

Responsibilities:
- Build prompts
- Call AI
- Save generated output
- Return output file path

Author: Raju Nalla
"""

from pathlib import Path

from config.config_loader import ConfigLoader
from modules.ai_client import AIClient
from modules.logger import get_logger
from modules.prompt_builder import PromptBuilder

logger = get_logger(__name__)


class BaseAIGenerator:
    """
    Base class for all AI generators.
    """

    TEMPLATE_NAME = ""
    OUTPUT_FILE = ""
    LOG_NAME = ""

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

    # ==========================================================
    # Existing API (Backward Compatible)
    # ==========================================================

    def generate_document(
        self,
        prompt_values: dict,
    ) -> str:
        """
        Generate document using the class template.
        """

        response = self.generate_content(
            self.TEMPLATE_NAME,
            prompt_values,
        )

        return self.save_document(
            response,
            self.OUTPUT_FILE,
        )

    # ==========================================================
    # New API
    # ==========================================================

    def generate_content(
        self,
        template_name: str,
        prompt_values: dict,
    ) -> str:
        """
        Generate AI content using any prompt template.
        """

        logger.info(
            f"Generating prompt: {template_name}"
        )

        prompt = self.prompt_builder.build_prompt(
            template_name,
            prompt_values,
        )

        logger.info(
            "Sending prompt to AI..."
        )

        response = self.ai_client.generate(
            prompt
        )

        return response

    def save_document(
        self,
        content: str,
        output_filename: str,
    ) -> str:
        """
        Save generated content.
        """

        output_file = (
            self.output_directory /
            output_filename
        )

        output_file.write_text(
            content,
            encoding="utf-8",
        )

        logger.info(
            f"Saved: {output_file}"
        )

        return str(output_file)