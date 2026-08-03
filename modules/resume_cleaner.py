"""
resume_cleaner.py

Extracts only the important sections from a parsed resume
to reduce prompt size for AI generation.

Author: Raju Nalla
"""

import re

from modules.logger import get_logger

logger = get_logger(__name__)


class ResumeCleaner:
    """
    Cleans and extracts important resume sections
    for AI prompt generation.
    """

    SECTION_MAP = {
        "summary": [
            "Professional Summary",
            "Summary",
            "Profile",
        ],
        "skills": [
            "Technical Skills",
            "Skills",
            "Core Skills",
        ],
        "experience": [
            "Professional Experience",
            "Work Experience",
            "Experience",
        ],
        "projects": [
            "Projects",
            "Project Experience",
        ],
    }

    def clean(
        self,
        resume_text: str,
    ) -> dict:

        logger.info(
            "Cleaning resume..."
        )

        result = {
            "summary": self._extract_section(
                resume_text,
                self.SECTION_MAP["summary"],
            ),
            "skills": self._extract_section(
                resume_text,
                self.SECTION_MAP["skills"],
            ),
            "experience": self._extract_section(
                resume_text,
                self.SECTION_MAP["experience"],
            ),
            "projects": self._extract_section(
                resume_text,
                self.SECTION_MAP["projects"],
            ),
        }

        logger.info(
            "Resume cleaned successfully."
        )

        return result

    # ---------------------------------------------------------

    def _extract_section(
        self,
        text: str,
        headers: list[str],
    ) -> str:

        lines = text.splitlines()

        start = None

        for index, line in enumerate(lines):

            current = line.strip().lower()

            if any(
                current == header.lower()
                for header in headers
            ):
                start = index + 1
                break

        if start is None:
            return ""

        collected = []

        for line in lines[start:]:

            stripped = line.strip()

            if not stripped:
                continue

            if self._is_section_header(stripped):
                break

            collected.append(stripped)

        return "\n".join(collected)

    # ---------------------------------------------------------

    def _is_section_header(
        self,
        line: str,
    ) -> bool:

        headers = []

        for values in self.SECTION_MAP.values():
            headers.extend(values)

        return any(
            line.lower() == header.lower()
            for header in headers
        )