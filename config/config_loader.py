"""
config_loader.py

Loads application configuration from settings.yaml.

Author: Raju Nalla
"""

from pathlib import Path

import yaml

from modules.logger import get_logger

logger = get_logger(__name__)


class ConfigLoader:
    """
    Loads configuration values from YAML.
    """

    def __init__(self, config_file="config/settings.yaml"):

        self.config_path = Path(config_file)

        if not self.config_path.exists():
            logger.error(f"Configuration file not found: {self.config_path}")
            raise FileNotFoundError(
                f"Configuration file '{config_file}' not found."
            )

        with open(self.config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

        logger.info("Configuration loaded successfully.")

    def get(self, key: str, default=None):
        """
        Retrieve nested configuration values using dot notation.

        Example:
            config.get("database.path")
            config.get("paths.prompts")
            config.get("ai.model")
        """

        value = self.config

        for part in key.split("."):

            if isinstance(value, dict):
                value = value.get(part)

            else:
                return default

            if value is None:
                return default

        return value