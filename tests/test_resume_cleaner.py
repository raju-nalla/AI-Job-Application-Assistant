from modules.resume_parser import ResumeParser
from modules.resume_cleaner import ResumeCleaner

resume = ResumeParser().parse(
    "data/resumes/raju_nalla_resume-DE.pdf"
)

cleaner = ResumeCleaner()

result = cleaner.clean(
    resume["resume_text"]
)

print(result["summary"])
print("=" * 80)
print(result["skills"])
print("=" * 80)
print(result["experience"][:1000])
print("=" * 80)
print(result["projects"])