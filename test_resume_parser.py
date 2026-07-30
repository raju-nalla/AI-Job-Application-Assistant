from modules.resume_parser import ResumeParser

parser = ResumeParser()

resume = parser.parse("data/resumes/raju_nalla_resume-DE.pdf")

print("=" * 60)

print("Name:")
print(resume["name"])

print()

print("Email:")
print(resume["email"])

print()

print("Phone:")
print(resume["phone"])

print()

print("Resume Preview:")
print(resume["resume_text"][:500])

print("=" * 60)