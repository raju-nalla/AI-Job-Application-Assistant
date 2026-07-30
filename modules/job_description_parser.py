"""
job_description_parser.py

Job Description parsing module for
AI Job Application Assistant.

Responsibilities:
- Read Job Description
- Extract company
- Extract job title
- Extract experience
- Return structured data

Author: Raju Nalla
"""

import re

from modules.file_reader import FileReader
from modules.logger import get_logger

logger = get_logger(__name__)


class JobDescriptionParser:
    """
    Parses Job Description documents.
    """

    def __init__(self):
        self.file_reader = FileReader()

    # ---------------------------------------------------------
    # Public Method
    # ---------------------------------------------------------

    def parse(self, file_path: str) -> dict:
        """
        Parses a Job Description.

        Parameters
        ----------
        file_path : str

        Returns
        -------
        dict
        """

        logger.info("Starting Job Description parsing...")

        text = self.file_reader.read(file_path)

        job_data = {
            "company": self._extract_company(text),
            "job_title": self._extract_job_title(text),
            "experience": self._extract_experience(text),
            "job_description": text
        }

        logger.info("Job Description parsed successfully.")

        return job_data

    # ---------------------------------------------------------
    # Private Methods
    # ---------------------------------------------------------

    def _extract_company(self, text: str) -> str:
        """
        Extract company name.
        Looks for 'Company:' first, otherwise returns empty.
        """

        match = re.search(r"Company\s*:\s*(.+)", text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

        return ""

    def _extract_job_title(self, text: str) -> str:
        """
        Assume first non-empty line is the job title.
        """

        for line in text.splitlines():
            line = line.strip()

            if line:
                return line

        return ""

    def _extract_experience(self, text: str) -> str:
        """
        Extract experience such as:
        4+ years
        5 years
        3-5 years
        """

        pattern = r"\d+\+?\s*(?:-|to)?\s*\d*\s*years?"

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group()

        return ""