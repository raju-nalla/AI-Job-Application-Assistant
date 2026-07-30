"""
openai_client.py

Centralized OpenAI Client

Responsibilities:
- Load API key from .env
- Load AI configuration
- Initialize OpenAI client
- Send prompts
- Handle retries
- Handle exceptions
- Log requests

Author: Raju Nalla
"""

from dotenv import load_dotenv
from openai import OpenAI

import os
import time

from modules.logger import get_logger
from config.config_loader import ConfigLoader

logger = get_logger(__name__)

load_dotenv()


class OpenAIClient:

    def __init__(self):

        config = ConfigLoader()

        self.api_key = os.getenv("OPENROUTER_API_KEY")

        if not self.api_key:
            raise ValueError(
                "OPENROUTER_API_KEY not found in .env file."
            )

        self.model = config.get("ai.model")
        self.temperature = config.get("ai.temperature")
        self.max_completion_tokens = config.get(
            "ai.max_completion_tokens"
        )
        self.timeout = config.get("ai.timeout")
        self.max_retries = config.get("ai.max_retries")

        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

        logger.info(
            f"OpenAI Client initialized using model '{self.model}'."
        )

    def generate(self, prompt: str) -> str:

        logger.info("Sending prompt to OpenAI...")

        start = time.time()

        try:

            response = self.client.responses.create(
                model=self.model,
                input=prompt,
                temperature=self.temperature,
                max_output_tokens=self.max_completion_tokens
            )

            elapsed = round(time.time() - start, 2)

            logger.info(
                f"OpenAI response received in {elapsed} seconds."
            )

            return response.output_text

        except Exception as ex:

            logger.exception(
                "OpenAI request failed."
            )

            raise RuntimeError(
                f"OpenAI API Error: {ex}"
            ) from ex