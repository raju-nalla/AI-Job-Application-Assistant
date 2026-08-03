"""
main.py

AI Job Application Assistant

Author: Raju Nalla
"""

from config.config_loader import ConfigLoader

from modules.workflow_builder import WorkflowBuilder
from modules.report_manager import ReportManager

from modules.resume_optimizer import ResumeOptimizer
from modules.cover_letter_generator import CoverLetterGenerator
from modules.interview_overview import InterviewOverview
from modules.technical_interview_guide import TechnicalInterviewGuide
from modules.behavioral_interview_guide import BehavioralInterviewGuide


def main():

    # ---------------------------------------------------------
    # Load Configuration
    # ---------------------------------------------------------

    config = ConfigLoader()

    resume_path = config.get("paths.resume")

    job_description_path = config.get(
        "paths.job_description"
    )

    # ---------------------------------------------------------
    # Build Workflow Context
    # ---------------------------------------------------------

    workflow = WorkflowBuilder()

    context = workflow.build(
        resume_path=resume_path,
        job_description_path=job_description_path,
    )

    # ---------------------------------------------------------
    # Initialize AI Generators
    # ---------------------------------------------------------

    resume_optimizer = ResumeOptimizer()

    cover_letter = CoverLetterGenerator()

    interview_overview = InterviewOverview()

    technical_guide = TechnicalInterviewGuide()

    behavioral_guide = BehavioralInterviewGuide()

    # ---------------------------------------------------------
    # Generate Reports
    # ---------------------------------------------------------

    manager = ReportManager()

    manager.run(
        context=context,
        resume_optimizer=resume_optimizer,
        cover_letter=cover_letter,
        interview_overview=interview_overview,
        technical_guide=technical_guide,
        behavioral_guide=behavioral_guide,
    )


if __name__ == "__main__":
    main()