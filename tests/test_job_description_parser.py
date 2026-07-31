from modules.job_description_parser import JobDescriptionParser

parser = JobDescriptionParser()

job = parser.parse("data/job_descriptions/sample_jd.txt")

print("=" * 60)

print("Company:")
print(job["company"])

print()

print("Job Title:")
print(job["job_title"])

print()

print("Experience:")
print(job["experience"])

print()

print("Job Description Preview:")
print(job["job_description"][:500])

print("=" * 60)