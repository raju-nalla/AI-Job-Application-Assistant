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
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "AI Job Application Assistant",
            },
        )

    def generate(self, prompt: str) -> str:

        logger.info("Sending prompt to AI...")

        start = time.time()

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                max_tokens=self.max_completion_tokens,
            )

            elapsed = round(time.time() - start, 2)

            logger.info(
                f"AI response received in {elapsed} seconds."
            )

            choice = response.choices[0]

            print("\n========== AI CLIENT ==========")
            print("Finish Reason :", choice.finish_reason)
            print("Content Type  :", type(choice.message.content))
            print("Content None  :", choice.message.content is None)

            if not choice.message.content:
                raise RuntimeError(
                    f"""
            Model returned no content.

            Finish Reason: {choice.finish_reason}

            The model likely reached its token/output limit.
            Reduce the prompt size or use a model with a larger context window.
            """
                )

            return choice.message.content

        except Exception as ex:

            logger.exception("AI request failed.")

            raise RuntimeError(
                f"AI API Error: {ex}"
            ) from ex

            logger.info("Sending prompt to AI...")

            start = time.time()

            try:

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    max_tokens=self.max_completion_tokens,
                )
                print("\n========== DEBUG ==========")
                print(type(response))
                print("output_text:", repr(response.output_text))

                if hasattr(response, "output"):
                    print("output:", response.output)

                print("===========================\n")

                elapsed = round(time.time() - start, 2)

                logger.info(
                    f"AI response received in {elapsed} seconds."
                )
                choice = response.choices[0]

                print("\n========== AI CLIENT ==========")
                print("Finish Reason :", choice.finish_reason)
                print("Content Type  :", type(choice.message.content))
                print("Content None  :", choice.message.content is None)

                if choice.message.content:
                    print("Content Preview:")
                    print(choice.message.content[:300])

                print("================================\n")

                return choice.message.content

            except Exception as ex:

                logger.exception("AI request failed.")

                raise RuntimeError(
                    f"AI API Error: {ex}"
                ) from ex

                logger.info("Sending prompt to AI...")

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    max_tokens=self.max_completion_tokens,
                )

                return response.choices[0].message.content