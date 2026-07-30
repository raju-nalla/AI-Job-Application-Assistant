"""
prompt_builder.py

Prompt Builder for AI Job Application Assistant.

Responsibilities:
- Load prompt templates
- Replace placeholders
- Validate placeholders
- Generate final prompts

Author: Raju Nalla
"""

from pathlib import Path
import re

from modules.logger import get_logger

logger = get_logger(__name__)


class PromptBuilder:
    """
    Builds prompts from template files.
    """

    def __init__(self, prompt_directory="prompts"):
        self.prompt_directory = Path(prompt_directory)

    def load_template(self, template_name: str) -> str:
        """
        Load a prompt template.
        """

        template_path = self.prompt_directory / template_name

        if not template_path.exists():
            logger.error(f"Template not found: {template_path}")
            raise FileNotFoundError(
                f"Prompt template '{template_name}' not found."
            )

        logger.info(f"Loading prompt template: {template_name}")

        return template_path.read_text(
            encoding="utf-8"
        )

    def get_placeholders(self, template: str) -> list[str]:
        """
        Return placeholders found in template.

        Example:
        {{resume}}
        {{job_description}}
        """

        return re.findall(
            r"\{\{(.*?)\}\}",
            template
        )

    def build_prompt(
    self,
    template_name: str,
    values: dict[str, str]
    ) -> str:
        """
        Build final prompt.
        """

        template = self.load_template(template_name)

        placeholders = self.get_placeholders(template)

        missing = [
            field
            for field in placeholders
            if field not in values
        ]

        if missing:
            logger.error(
                f"Missing placeholders: {missing}"
            )

            raise ValueError(
                f"Missing values for placeholders: {missing}"
            )

        prompt = template

        for key, value in values.items():
            prompt = prompt.replace(
                f"{{{{{key}}}}}",
                str(value)
            )

        logger.info("Prompt generated successfully.")

        return prompt