"""
resume_optimizer.py

AI Resume Optimizer

Responsibilities:
- Build optimization prompt
- Send prompt to AI
- Save optimized resume
- Return optimized resume

Author: Raju Nalla
"""

from pathlib import Path

from config import config
from modules.ai_client import AIClient
from modules.logger import get_logger
from modules.prompt_builder import PromptBuilder

logger = get_logger(__name__)


class ResumeOptimizer:
    """
    AI-powered Resume Optimizer.
    """

    def __init__(self):

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

    def optimize(
        self,
        resume_text: str,
        job_description: str,
        ats_report: str
    ) -> str:
        """
        Generate an optimized resume using AI.
        """

        logger.info("Generating resume optimization prompt...")

        prompt = self.prompt_builder.build_prompt(
            "resume_optimizer_prompt.txt",
            {
                "resume": resume_text,
                "job_description": job_description,
                "ats_report": ats_report,
            },
        )

        logger.info("Sending prompt to AI model...")

        optimized_resume = self.ai_client.generate(prompt)

        output_file = (
            self.output_directory /
            "optimized_resume.md"
        )

        output_file.write_text(
            optimized_resume,
            encoding="utf-8"
        )

        logger.info(
            f"Optimized resume saved to {output_file}"
        )

        return str(output_file)