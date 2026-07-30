"""
ats_report_generator.py

ATS Report Generator for
AI Job Application Assistant.

Responsibilities:
- Generate formatted ATS report
- Display ATS analysis
- Save ATS report to file

Author: Raju Nalla
"""

from pathlib import Path

from modules.logger import get_logger

logger = get_logger(__name__)


class ATSReportGenerator:
    """
    Generates ATS Analysis Report.
    """

    def generate(self, report: dict) -> str:

        logger.info("Generating ATS report...")

        lines = []

        lines.append("=" * 70)
        lines.append("               ATS ANALYSIS REPORT")
        lines.append("=" * 70)

        lines.append("")
        lines.append(f"Overall ATS Score : {report['overall_score']}%")

        lines.append("")
        lines.append("-" * 70)
        lines.append("Category Scores")
        lines.append("-" * 70)

        for category, score in report["category_scores"].items():
            lines.append(f"{category:<35} {score}%")

        lines.append("")
        lines.append("-" * 70)
        lines.append("Strengths")
        lines.append("-" * 70)

        if report["strengths"]:
            for item in report["strengths"]:
                lines.append(f"✔ {item}")
        else:
            lines.append("None")

        lines.append("")
        lines.append("-" * 70)
        lines.append("Areas for Improvement")
        lines.append("-" * 70)

        if report["weaknesses"]:
            for item in report["weaknesses"]:
                lines.append(f"✘ {item}")
        else:
            lines.append("None")

        lines.append("")
        lines.append("-" * 70)
        lines.append("Missing Skills")
        lines.append("-" * 70)

        if report["missing_skills"]:
            for skill in report["missing_skills"]:
                lines.append(
                    f"- {skill['name']} ({skill['priority']})"
                )
        else:
            lines.append("None")

        lines.append("")
        lines.append("-" * 70)
        lines.append("Recommendations")
        lines.append("-" * 70)

        if report["recommendations"]:
            for recommendation in report["recommendations"]:
                lines.append(f"- {recommendation}")
        else:
            lines.append("No recommendations.")

        lines.append("")
        lines.append("=" * 70)

        logger.info("ATS report generated successfully.")

        return "\n".join(lines)

    def save(self,
             report_text: str,
             output_file: str):

        """
        Save report to text file.
        """

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output_path.write_text(
            report_text,
            encoding="utf-8"
        )

        logger.info(
            f"ATS report saved to {output_file}"
        )