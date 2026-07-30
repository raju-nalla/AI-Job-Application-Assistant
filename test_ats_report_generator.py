from modules.file_reader import FileReader
from modules.skill_extractor import SkillExtractor
from modules.ats_engine import ATSEngine
from modules.ats_report_generator import ATSReportGenerator

reader = FileReader()
extractor = SkillExtractor()
engine = ATSEngine()
report_generator = ATSReportGenerator()

resume = reader.read(
    "data/resumes/raju_nalla_resume-DE.pdf"
)

jd = reader.read(
    "data/job_descriptions/sample_jd.txt"
)

resume_skills = extractor.extract_skills(resume)
jd_skills = extractor.extract_skills(jd)

ats_report = engine.compare(
    resume_skills,
    jd_skills
)

report = report_generator.generate(
    ats_report
)

print(report)

report_generator.save(
    report,
    "reports/ats_report.txt"
)