from modules.resume_parser import ResumeParser
from modules.resume_cleaner import ResumeCleaner

from modules.job_description_parser import JobDescriptionParser
from modules.job_description_cleaner import JobDescriptionCleaner

from modules.prompt_context_builder import PromptContextBuilder

resume = ResumeParser().parse(
    "data/resumes/raju_nalla_resume-DE.pdf"
)

resume = ResumeCleaner().clean(
    resume["resume_text"]
)

resume["name"] = "Raju Nalla"

jd = JobDescriptionParser().parse(
    "data/job_descriptions/senior_data_engineer_ssis.txt"
)

jd = JobDescriptionCleaner().clean(
    jd["job_description"]
)

context = PromptContextBuilder().build(
    resume,
    jd,
    "ATS Score : 84%"
)

print("=" * 80)

for key, value in context.items():

    print(f"{key}")

    print("-" * 40)

    print(str(value)[:300])

    print()