"""
prompt_context_builder.py

Builds a compact AI prompt context shared by
all AI generators.

Author: Raju Nalla
"""

from modules.logger import get_logger

logger = get_logger(__name__)


class PromptContextBuilder:

    def build(
        self,
        resume: dict,
        job_description: dict,
        ats_report: str,
    ) -> dict:

        logger.info("Building AI Prompt Context...")

        # --------------------------------------------------
        # Old Prompt Compatibility
        # --------------------------------------------------

        resume_text = f"""
# Professional Summary

{resume.get("summary","")}

# Technical Skills

{resume.get("skills","")}

# Professional Experience

{resume.get("experience","")}

# Projects

{resume.get("projects","")}
"""

        context = {

            # ==========================
            # OLD PLACEHOLDERS
            # ==========================

            "resume": resume_text,

            "job_description": job_description.get(
                "description",
                "",
            ),

            "ats_report": ats_report,

            # ==========================
            # NEW PLACEHOLDERS
            # ==========================

            "candidate_name": resume.get(
                "name",
                "",
            ),

            "summary": resume.get(
                "summary",
                "",
            ),

            "skills": resume.get(
                "skills",
                "",
            ),

            "experience": resume.get(
                "experience",
                "",
            ),

            "projects": resume.get(
                "projects",
                "",
            ),

            "job_role": job_description.get(
                "role",
                "",
            ),

            "company": job_description.get(
                "company",
                "",
            ),

            "required_experience": job_description.get(
                "experience",
                "",
            ),

            "required_skills": ", ".join(
                job_description.get(
                    "skills",
                    [],
                )
            ),

        }

        logger.info(
            "AI Prompt Context built successfully."
        )

        return context