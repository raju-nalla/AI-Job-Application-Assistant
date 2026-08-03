"""
resume_optimizer.py

AI Resume Optimizer

Responsibilities:
- Generate an ATS-optimized resume tailored to a job description.

Author: Raju Nalla
"""

from modules.base_ai_generator import BaseAIGenerator


class ResumeOptimizer(BaseAIGenerator):
    """
    AI-powered Resume Optimizer.
    """

    TEMPLATE_NAME = "resume/resume_optimizer_prompt.txt"
    OUTPUT_FILE = "optimized_resume.md"
    LOG_NAME = "Resume Optimizer"

    def generate(self, context: dict) -> str:
        """
        Generate an optimized resume using the shared context.
        """

        return self.generate_document(
            template_name=self.TEMPLATE_NAME,
            prompt_values=context,
            output_file=self.OUTPUT_FILE,
        )