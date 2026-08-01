"""
test_interview_preparation_guide.py

Test AI Interview Preparation Guide

Author: Raju Nalla
"""

from pathlib import Path

from modules.ats_engine import ATSEngine
from modules.ats_report_generator import ATSReportGenerator
from modules.interview_preparation_guide import (
    InterviewPreparationGuide,
)
from modules.job_description_parser import JobDescriptionParser
from modules.resume_parser import ResumeParser
from modules.skill_extractor import SkillExtractor


def main():

    resume_file = Path(
        "data/resumes/raju_nalla_resume-DE.pdf"
    )

    jd_file = Path(
        "data/job_descriptions/senior_data_engineer_ssis.txt"
    )

    resume_parser = ResumeParser()
    jd_parser = JobDescriptionParser()

    resume = resume_parser.parse(
        str(resume_file)
    )

    job = jd_parser.parse(
        str(jd_file)
    )

    extractor = SkillExtractor()

    resume_skills = extractor.extract_skills(
        resume["resume_text"]
    )

    jd_skills = extractor.extract_skills(
        job["job_description"]
    )

    ats = ATSEngine()

    ats_result = ats.compare(
        resume_skills,
        jd_skills
    )

    report_generator = ATSReportGenerator()

    ats_report = report_generator.generate(
        ats_result
    )

    generator = InterviewPreparationGuide()

    output = generator.generate(
        resume_text=resume["resume_text"],
        job_description=job["job_description"],
        ats_report=ats_report,
    )

    print()

    print("=" * 70)
    print("INTERVIEW PREPARATION GUIDE GENERATED")
    print("=" * 70)

    print(f"Candidate : {resume['name']}")
    print(f"Output    : {output}")

    print("=" * 70)


if __name__ == "__main__":
    main()