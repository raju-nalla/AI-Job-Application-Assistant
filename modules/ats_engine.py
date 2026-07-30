"""
ats_engine.py

Enterprise ATS Matching Engine for
AI Job Application Assistant.

Responsibilities:
- Compare Resume Skills
- Compare Job Description Skills
- Calculate Weighted ATS Score
- Calculate Category Scores
- Identify Strengths & Weaknesses
- Generate Recommendations

Author: Raju Nalla
"""

from modules.logger import get_logger

logger = get_logger(__name__)


class ATSEngine:
    """
    Enterprise ATS Matching Engine.
    """

    PRIORITY_WEIGHTS = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    def compare(self,
                resume_skills: dict,
                jd_skills: dict) -> dict:

        logger.info("Starting ATS comparison...")

        matched_skills = []
        missing_skills = []
        extra_skills = []

        category_scores = {}

        total_weight = 0
        matched_weight = 0

        # ----------------------------------------------------
        # Category Comparison
        # ----------------------------------------------------

        for category, jd_items in jd_skills.items():

            resume_items = resume_skills.get(category, [])

            resume_lookup = {
                skill["name"]: skill
                for skill in resume_items
            }

            category_total = 0
            category_matched = 0

            for jd_skill in jd_items:

                name = jd_skill["name"]

                priority = jd_skill["priority"]

                weight = self.PRIORITY_WEIGHTS.get(priority, 1)

                total_weight += weight
                category_total += weight

                if name in resume_lookup:

                    matched_skills.append(jd_skill)

                    matched_weight += weight
                    category_matched += weight

                else:

                    missing_skills.append(jd_skill)

            score = 0

            if category_total > 0:

                score = round(
                    (category_matched / category_total) * 100,
                    2
                )

            category_scores[category] = score

        # ----------------------------------------------------
        # Extra Skills
        # ----------------------------------------------------

        jd_names = {
            skill["name"]
            for skills in jd_skills.values()
            for skill in skills
        }

        for skills in resume_skills.values():

            for skill in skills:

                if skill["name"] not in jd_names:

                    extra_skills.append(skill)

        # ----------------------------------------------------
        # Overall Score
        # ----------------------------------------------------

        overall_score = 0

        if total_weight > 0:

            overall_score = round(
                (matched_weight / total_weight) * 100,
                2
            )

        # ----------------------------------------------------
        # Strengths
        # ----------------------------------------------------

        strengths = []

        weaknesses = []

        for category, score in category_scores.items():

            if score >= 80:

                strengths.append(category)

            elif score < 50:

                weaknesses.append(category)

        # ----------------------------------------------------
        # Recommendations
        # ----------------------------------------------------

        recommendations = []

        for skill in missing_skills:

            if skill["priority"] == "High":

                recommendations.append(
                    f"Add '{skill['name']}' to strengthen your resume."
                )

        logger.info("ATS comparison completed.")

        return {

            "overall_score": overall_score,

            "category_scores": category_scores,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "extra_skills": extra_skills,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "recommendations": recommendations

        }