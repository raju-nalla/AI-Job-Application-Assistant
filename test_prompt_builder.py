from modules.prompt_builder import PromptBuilder

from config.config_loader import ConfigLoader

config = ConfigLoader()

builder = PromptBuilder(
    config.get("paths.prompts")
)

prompt = builder.build_prompt(
    "resume_optimizer_prompt.txt",
    {
        "resume": "Python, Azure Data Factory, Databricks",
        "job_description": "Looking for Azure Data Engineer with Airflow experience.",
        "ats_report": """
Overall Score: 80%

Missing Skills:
- Apache Airflow
- Docker
"""
    }
)

print(prompt)