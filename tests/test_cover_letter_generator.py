"""
test_cover_letter_generator.py

Test AI Cover Letter Generator

Author: Raju Nalla
"""

from pathlib import Path

from modules.cover_letter_generator import CoverLetterGenerator
from modules.resume_parser import ResumeParser
from modules.job_description_parser import JobDescriptionParser


def main():

    # -----------------------------
    # Input Files
    # -----------------------------

    resume_file = Path(
        "data/resumes/raju_nalla_resume-DE.pdf"
    )

    jd_file = Path(
        "data/job_descriptions/senior_data_engineer_ssis.txt"
    )

    # -----------------------------
    # Parse Resume
    # -----------------------------

    resume_parser = ResumeParser()

    resume_data = resume_parser.parse(
        str(resume_file)
    )

    resume_text = resume_data["resume_text"]

    candidate_name = resume_data["name"]

    # -----------------------------
    # Parse JD
    # -----------------------------

    jd_parser = JobDescriptionParser()

    jd_data = jd_parser.parse(
        str(jd_file)
    )

    job_description = jd_data["job_description"]

    # -----------------------------
    # Generate Cover Letter
    # -----------------------------

    generator = CoverLetterGenerator()

    output_path = generator.generate(
        resume_text=resume_text,
        job_description=job_description,
        candidate_name=candidate_name
    )

    print()

    print("=" * 70)
    print("COVER LETTER GENERATED")
    print("=" * 70)

    print(f"Candidate : {candidate_name}")
    print(f"Output    : {output_path}")

    print("=" * 70)


if __name__ == "__main__":
    main()