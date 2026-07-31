"""
ai_client.py

Centralized AI Client

Responsibilities:
- Load API key from .env
- Load AI configuration
- Initialize AI client
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
from config import config

logger = get_logger(__name__)

load_dotenv()


class AIClient:

    def __init__(self):


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
            api_key=self.api_key,
            base_url="https://openrouter.ai/api/v1",
            timeout=self.timeout,
            max_retries=self.max_retries,
        )
        logger.info(
            f"AI Client initialized using model '{self.model}'."
        )

    def generate(self, prompt: str) -> str:

        logger.info("Sending prompt to AI...")

        start = time.time()

        try:

            response = self.client.responses.create(
                model=self.model,
                input=prompt,
                max_output_tokens=self.max_completion_tokens
            )

            elapsed = round(time.time() - start, 2)

            logger.info(
                f"AI response received in {elapsed} seconds."
            )

            return response.output_text

        except Exception as ex:

            logger.exception(
                "AI request failed."
            )

            raise RuntimeError(
                f"AI API Error: {ex}"
            ) from ex