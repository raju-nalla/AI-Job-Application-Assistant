"""
workflow_builder.py

Builds the complete AI Job Application Assistant workflow.

Author: Raju Nalla
"""

from modules.resume_parser import ResumeParser
from modules.resume_cleaner import ResumeCleaner

from modules.job_description_parser import JobDescriptionParser
from modules.job_description_cleaner import JobDescriptionCleaner

from modules.skill_extractor import SkillExtractor

from modules.ats_engine import ATSEngine
from modules.ats_report_generator import ATSReportGenerator

from modules.prompt_context_builder import PromptContextBuilder


class WorkflowBuilder:
    """
    Builds the complete AI workflow.
    """

    def __init__(self):

        self.resume_parser = ResumeParser()
        self.resume_cleaner = ResumeCleaner()

        self.jd_parser = JobDescriptionParser()
        self.jd_cleaner = JobDescriptionCleaner()

        self.skill_extractor = SkillExtractor()

        self.ats_engine = ATSEngine()
        self.ats_report_generator = ATSReportGenerator()

        self.prompt_context_builder = PromptContextBuilder()

    # ==========================================================
    # Build Workflow
    # ==========================================================

    def build(
        self,
        resume_path: str,
        job_description_path: str,
    ) -> dict:

        # ------------------------------------------------------
        # Parse Resume
        # ------------------------------------------------------

        resume = self.resume_parser.parse(
            resume_path
        )

        resume_sections = self.resume_cleaner.clean(
            resume["resume_text"]
        )

        resume.update(resume_sections)

        # ------------------------------------------------------
        # Parse Job Description
        # ------------------------------------------------------

        job_description = self.jd_parser.parse(
            job_description_path
        )

        job_description = self.jd_cleaner.clean(
            job_description
        )

        # ------------------------------------------------------
        # Extract Skills
        # ------------------------------------------------------

        resume_skills = self.skill_extractor.extract_skills(
            resume["resume_text"]
        )

        jd_skills = self.skill_extractor.extract_skills(
            job_description["description"]
        )

        # ------------------------------------------------------
        # ATS Comparison
        # ------------------------------------------------------

        ats_result = self.ats_engine.compare(
            resume_skills,
            jd_skills,
        )

        ats_report = self.ats_report_generator.generate(
            ats_result
        )

        # ------------------------------------------------------
        # Build AI Context
        # ------------------------------------------------------

        context = self.prompt_context_builder.build(
            resume=resume,
            job_description=job_description,
            ats_report=ats_report,
        )

        return context