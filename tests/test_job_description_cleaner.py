from modules.job_description_parser import JobDescriptionParser
from modules.job_description_cleaner import JobDescriptionCleaner


jd = JobDescriptionParser().parse(
    "data/job_descriptions/senior_data_engineer_ssis.txt"
)

cleaner = JobDescriptionCleaner()

result = cleaner.clean(
    jd["job_description"]
)

print("=" * 80)
print("ROLE")
print("=" * 80)
print(result["role"])

print()

print("=" * 80)
print("DESCRIPTION")
print("=" * 80)
print(result["description"][:2000])   # preview first 2000 characters