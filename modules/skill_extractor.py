"""
skill_extractor.py

Skill extraction module for
AI Job Application Assistant.

Responsibilities:
- Load skills from JSON
- Extract skills from resume/JD
- Resolve aliases
- Return canonical skills with metadata

Author: Raju Nalla
"""

import json
from pathlib import Path

from modules.logger import get_logger

logger = get_logger(__name__)


class SkillExtractor:
    """
    Extracts technical skills from text using
    a centralized skills.json repository.
    """

    def __init__(self):

        self.skills_file = Path("data/skills/skills.json")
        self.skills = self._load_skills()

    # ---------------------------------------------------------
    # Private Methods
    # ---------------------------------------------------------

    def _load_skills(self) -> dict:
        """
        Load skills.json
        """

        try:

            with open(self.skills_file, "r", encoding="utf-8") as file:
                skills = json.load(file)

            logger.info("Skills loaded successfully.")

            return skills

        except Exception as error:

            logger.error(f"Unable to load skills.json : {error}")
            raise

    # ---------------------------------------------------------
    # Public Method
    # ---------------------------------------------------------

    def extract_skills(self, text: str) -> dict:
        """
        Extract skills from text.

        Parameters
        ----------
        text : str

        Returns
        -------
        dict
        """

        logger.info("Extracting skills...")

        text = text.lower()

        extracted = {}

        for category, skills in self.skills.items():

            matched = []

            for skill in skills:

                canonical = skill["name"]
                aliases = skill["aliases"]
                priority = skill["priority"]

                search_terms = [canonical] + aliases

                found = False

                for term in search_terms:

                    if term.lower() in text:
                        found = True
                        break

                if found:

                    matched.append(
                        {
                            "name": canonical,
                            "priority": priority
                        }
                    )

            if matched:

                extracted[category] = matched

        logger.info("Skill extraction completed.")

        return extracted