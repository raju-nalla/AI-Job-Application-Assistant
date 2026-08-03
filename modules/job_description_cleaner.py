"""
job_description_cleaner.py

Cleans and extracts important information from a Job Description.

Author: Raju Nalla
"""

import re

from modules.logger import get_logger

logger = get_logger(__name__)


class JobDescriptionCleaner:
    """
    Cleans a Job Description and extracts
    useful information for AI prompts.
    """

    def clean(
        self,
        job_description: str | dict,
    ) -> dict:

        logger.info(
            "Cleaning Job Description..."
        )

        if isinstance(job_description, dict):

            job_description = job_description.get(
                "job_description",
                ""
            )

        job_description = job_description.strip()

        result = {

            "role": self._extract_role(job_description),

            "company": self._extract_company(job_description),

            "experience": self._extract_experience(job_description),

            "skills": self._extract_skills(job_description),

            "description": job_description,

        }

        logger.info(
            "Job Description cleaned successfully."
        )

        return result

    # ---------------------------------------------------------

    def _extract_role(
        self,
        text: str,
    ) -> str:

        for line in text.splitlines():

            line = line.strip()

            if line and len(line) < 80:

                return line

        return ""

    # ---------------------------------------------------------

    def _extract_company(
        self,
        text: str,
    ) -> str:

        match = re.search(
            r"Company\s*:\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:

            return match.group(1).strip()

        return ""

    # ---------------------------------------------------------

    def _extract_experience(
        self,
        text: str,
    ) -> str:

        pattern = r"\d+\+?\s*(?:-|to)?\s*\d*\s*years?"

        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:

            return match.group()

        return ""

    # ---------------------------------------------------------

    def _extract_skills(
        self,
        text: str,
    ) -> list[str]:

        keywords = [

            "python",
            "sql",
            "pyspark",
            "spark",
            "azure",
            "adf",
            "databricks",
            "synapse",
            "snowflake",
            "aws",
            "gcp",
            "ssis",
            "informatica",
            "fabric",
            "power bi",
            "airflow",
            "dbt",
            "delta lake",
            "git",
            "devops",
            "etl",

        ]

        text_lower = text.lower()

        skills = []

        for skill in keywords:

            if skill.lower() in text_lower:

                skills.append(skill)

        return sorted(set(skills))