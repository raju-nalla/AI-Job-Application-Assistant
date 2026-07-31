from modules.resume_optimizer import ResumeOptimizer

resume = """
Raju Nalla

Azure Data Engineer

Skills:
Python
PySpark
ADF
Azure Databricks
SQL
"""

job_description = """
Looking for an Azure Data Engineer
with PySpark, Databricks,
Snowflake and SQL.
"""

ats_report = """
ATS Score : 80%

Missing Skills:
- Snowflake

Recommendation:
Mention Snowflake project experience.
"""

optimizer = ResumeOptimizer()

result = optimizer.optimize(
    resume,
    job_description,
    ats_report
)

print(result)