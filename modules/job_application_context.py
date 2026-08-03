"""
job_application_context.py

Shared context object used across all AI generators.

Author: Raju Nalla
"""

from dataclasses import dataclass, field


@dataclass
class JobApplicationContext:
    """
    Shared data for the entire application.
    """

    candidate_name: str = ""

    resume_text: str = ""

    job_description: str = ""

    resume_skills: list[str] = field(default_factory=list)

    jd_skills: list[str] = field(default_factory=list)

    ats_report: str = ""

    ats_score: float = 0.0

    matched_skills: list[str] = field(default_factory=list)

    missing_skills: list[str] = field(default_factory=list)