"""
resume_parser.py

Resume parsing module for
AI Job Application Assistant.

Responsibilities:
- Read resume file
- Extract basic information
- Return structured resume data

Author: Raju Nalla
"""

import re

from modules.file_reader import FileReader
from modules.logger import get_logger

logger = get_logger(__name__)


class ResumeParser:
    """
    Parses resume files and extracts structured information.
    """

    def __init__(self):
        self.file_reader = FileReader()

    # ---------------------------------------------------------
    # Public Method
    # ---------------------------------------------------------

    def parse(self, file_path: str) -> dict:
        """
        Parses a resume and returns structured data.

        Parameters
        ----------
        file_path : str
            Resume file path.

        Returns
        -------
        dict
            Parsed resume information.
        """

        logger.info("Starting resume parsing...")

        text = self.file_reader.read(file_path)

        resume_data = {
            "name": self._extract_name(text),
            "email": self._extract_email(text),
            "phone": self._extract_phone(text),
            "resume_text": text
        }

        logger.info("Resume parsed successfully.")

        return resume_data

    # ---------------------------------------------------------
    # Private Methods
    # ---------------------------------------------------------

    def _extract_name(self, text: str) -> str:
        """
        Extract candidate name.
        Assumes the first non-empty line is the name.
        """

        lines = text.splitlines()

        for line in lines:
            line = line.strip()

            if line:
                return line

        return ""

    def _extract_email(self, text: str) -> str:
        """
        Extract email address.
        """

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        return match.group() if match else ""

    def _extract_phone(self, text: str) -> str:
        """
        Extract phone number.
        """

        pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}"

        match = re.search(pattern, text)

        return match.group() if match else ""