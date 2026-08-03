"""
report_manager.py

Coordinates the complete AI Job Application Assistant workflow.

Author: Raju Nalla
"""

import time

from modules.logger import get_logger

logger = get_logger(__name__)


class ReportManager:
    """
    Coordinates the complete AI report generation workflow.
    """

    def __init__(self):
        self.start_time = None

    # ==========================================================
    # Generate All Reports
    # ==========================================================

    def generate_reports(
        self,
        context: dict,
        resume_optimizer,
        cover_letter,
        interview_overview,
        technical_guide,
        behavioral_guide,
    ):
        """
        Generate every AI report using the shared context.
        """

        logger.info("Generating Resume Optimizer...")
        resume_optimizer.generate(context)

        logger.info("Generating Cover Letter...")
        cover_letter.generate(context)

        logger.info("Generating Interview Overview...")
        interview_overview.generate(context)

        logger.info("Generating Technical Interview Guide...")
        technical_guide.generate(context)

        logger.info("Generating Behavioral Interview Guide...")
        behavioral_guide.generate(context)

    # ==========================================================
    # Print Summary
    # ==========================================================

    def print_summary(self):

        elapsed = round(
            time.time() - self.start_time,
            2,
        )

        print()
        print("=" * 60)
        print(" AI JOB APPLICATION ASSISTANT ")
        print("=" * 60)

        print("✓ Resume Optimizer Generated")
        print("✓ Cover Letter Generated")
        print("✓ Interview Overview Generated")
        print("✓ Technical Interview Guide Generated")
        print("✓ Behavioral Interview Guide Generated")

        print("-" * 60)

        print("Reports Folder : reports/")
        print(f"Execution Time : {elapsed} sec")

        print("=" * 60)

    # ==========================================================
    # Run
    # ==========================================================

    def run(
        self,
        context: dict,
        resume_optimizer,
        cover_letter,
        interview_overview,
        technical_guide,
        behavioral_guide,
    ):
        """
        Execute the entire report generation workflow.
        """

        self.start_time = time.time()

        self.generate_reports(
            context=context,
            resume_optimizer=resume_optimizer,
            cover_letter=cover_letter,
            interview_overview=interview_overview,
            technical_guide=technical_guide,
            behavioral_guide=behavioral_guide,
        )

        self.print_summary()