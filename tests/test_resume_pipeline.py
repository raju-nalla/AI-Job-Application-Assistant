"""
test_resume_pipeline.py

End-to-End Resume Pipeline Test

Flow:
Resume -> Resume Parser -> Skill Extractor
                 |
                 v
Job Description -> JD Parser -> Skill Extractor
                 |
                 v
             ATS Engine
                 |
                 v
        ATS Report Generator
"""

from pathlib import Path
from modules.resume_optimizer import ResumeOptimizer
from modules.resume_parser import ResumeParser
from modules.job_description_parser import JobDescriptionParser
from modules.skill_extractor import SkillExtractor
from modules.ats_engine import ATSEngine
from modules.ats_report_generator import ATSReportGenerator
from modules.logger import get_logger

logger = get_logger(__name__)


def main():

    try:

        logger.info("=" * 70)
        logger.info("STARTING END-TO-END RESUME PIPELINE")
        logger.info("=" * 70)

        # --------------------------------------------------
        # Input Files
        # --------------------------------------------------

        resume_file = Path("data/resumes/raju_nalla_resume-DE.pdf")

        jd_file = Path(
            "data/job_descriptions/senior_data_engineer_ssis.txt"
        )

        report_output = Path(
            "reports/ats_report.txt"
        )

        # --------------------------------------------------
        # Initialize Modules
        # --------------------------------------------------

        resume_parser = ResumeParser()
        jd_parser = JobDescriptionParser()

        skill_extractor = SkillExtractor()

        ats_engine = ATSEngine()

        report_generator = ATSReportGenerator()
        resume_optimizer = ResumeOptimizer()
        

        # --------------------------------------------------
        # Parse Resume
        # --------------------------------------------------

        logger.info("Parsing Resume...")

        resume_data = resume_parser.parse(str(resume_file))

        resume_text = resume_data["resume_text"]

        # --------------------------------------------------
        # Parse Job Description
        # --------------------------------------------------

        logger.info("Parsing Job Description...")

        jd_data = jd_parser.parse(str(jd_file))

        job_description = jd_data["job_description"]

        # --------------------------------------------------
        # Extract Skills
        # --------------------------------------------------

        logger.info("Extracting Resume Skills...")

        resume_skills = skill_extractor.extract_skills(
            resume_text
        )

        logger.info("Extracting JD Skills...")

        jd_skills = skill_extractor.extract_skills(
            job_description
        )

        # --------------------------------------------------
        # ATS Comparison
        # --------------------------------------------------

        logger.info("Running ATS Comparison...")

        ats_result = ats_engine.compare(
            resume_skills,
            jd_skills
        )

        # --------------------------------------------------
        # Generate ATS Report
        # --------------------------------------------------

        logger.info("Generating ATS Report...")

        report_text = report_generator.generate(
            ats_result
        )

        report_generator.save(
            report_text,
            str(report_output)
        )
        # --------------------------------------------------
        # AI Resume Optimization
        # --------------------------------------------------

        logger.info("Optimizing Resume using AI...")

        optimized_resume_path = resume_optimizer.optimize(
            resume_text=resume_text,
            job_description=job_description,
            ats_report=report_text
        )

        print("\n" + "=" * 70)
        print("AI RESUME OPTIMIZATION COMPLETED")
        print("=" * 70)
        print(f"Optimized Resume : {optimized_resume_path}")
        print("=" * 70)

        # --------------------------------------------------
        # Summary
        # --------------------------------------------------

        print("\n" + "=" * 70)
        print("END-TO-END PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 70)

        print(f"Candidate              : {resume_data['name']}")
        print(f"Job Title              : {jd_data['job_title']}")
        print(f"Company                : {jd_data['company']}")
        print(f"Overall ATS Score      : {ats_result['overall_score']}%")
        print(f"ATS Report             : {report_output}")
        print(f"Optimized Resume       : {optimized_resume_path}")

        print("=" * 70)

        logger.info("Pipeline completed successfully.")

    except Exception as error:

        logger.exception(
            f"Pipeline failed : {error}"
        )

        raise


if __name__ == "__main__":
    main()