from pprint import pprint

from modules.ats_engine import ATSEngine
from modules.file_reader import FileReader
from modules.skill_extractor import SkillExtractor

reader = FileReader()
extractor = SkillExtractor()
engine = ATSEngine()

resume_text = reader.read(
    "data/resumes/raju_nalla_resume-DE.pdf"
)

jd_text = reader.read(
    "data/job_descriptions/sample_jd.txt"
)

resume_skills = extractor.extract_skills(resume_text)

jd_skills = extractor.extract_skills(jd_text)

report = engine.compare(
    resume_skills,
    jd_skills
)

print("=" * 80)
print("ENTERPRISE ATS REPORT")
print("=" * 80)

pprint(report)

print("=" * 80)