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
            exist_ok=True,
        )

    # ==========================================================
    # Generate AI Content
    # ==========================================================

    def generate_content(
        self,
        template_name: str,
        prompt_values: dict,
    ) -> str:
        """
        Build the prompt and send it to the AI model.
        """

        logger.info(
            f"Building prompt: {template_name}"
        )

        prompt = self.prompt_builder.build_prompt(
            template_name=template_name,
            prompt_values=prompt_values,
        )

        logger.info("Sending prompt to AI...")

        return self.ai_client.generate(prompt)

    # ==========================================================
    # Generate Complete Document
    # ==========================================================

    def generate_document(
        self,
        template_name: str,
        prompt_values: dict,
        output_file: str,
    ) -> str:
        """
        Generate AI content and save it as a document.
        """

        content = self.generate_content(
            template_name=template_name,
            prompt_values=prompt_values,
        )

        return self.save_document(
            content=content,
            output_filename=output_file,
        )

    # ==========================================================
    # Save Document
    # ==========================================================

    def save_document(
        self,
        content: str,
        output_filename: str,
    ) -> str:
        """
        Save generated content into the reports folder.
        """

        output_path = self.output_directory / output_filename

        output_path.write_text(
            content,
            encoding="utf-8",
        )

        logger.info(
            f"Saved report: {output_path}"
        )

        return str(output_path)