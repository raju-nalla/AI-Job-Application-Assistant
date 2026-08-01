"""
resume_optimizer.py

AI Resume Optimizer

Responsibilities:
- Generate optimized resume

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

    def optimize(
        self,
        resume_text: str,
        job_description: str,
        ats_report: str,
    ) -> str:
        """
        Generate optimized resume.
        """

        prompt_values = {
            "resume": resume_text,
            "job_description": job_description,
            "ats_report": ats_report,
        }

        return self.generate_document(
            prompt_values
        )