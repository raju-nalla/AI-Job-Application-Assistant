"""
test_technical_interview.py

Tests Technical Interview Guide.

Author: Raju Nalla
"""

from pathlib import Path

from modules.ats_engine import ATSEngine
from modules.ats_report_generator import ATSReportGenerator
from modules.job_description_parser import JobDescriptionParser
from modules.resume_parser import ResumeParser
from modules.skill_extractor import SkillExtractor
from modules.technical_interview_guide import TechnicalInterviewGuide


def main():

    resume = ResumeParser().parse(
        "data/resumes/raju_nalla_resume-DE.pdf"
    )

    job = JobDescriptionParser().parse(
        "data/job_descriptions/senior_data_engineer_ssis.txt"
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
        jd_skills,
    )

    ats_report = ATSReportGenerator().generate(
        ats_result
    )

    guide = TechnicalInterviewGuide()

    output = guide.generate(
        resume["resume_text"],
        job["job_description"],
        ats_report,
    )

    print("\n" + "=" * 70)
    print("TECHNICAL INTERVIEW GUIDE GENERATED")
    print("=" * 70)
    print(output)
    print("=" * 70)


if __name__ == "__main__":
    main()