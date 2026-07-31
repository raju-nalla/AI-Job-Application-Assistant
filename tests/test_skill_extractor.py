from pprint import pprint

from modules.file_reader import FileReader
from modules.skill_extractor import SkillExtractor

reader = FileReader()
extractor = SkillExtractor()

text = reader.read(
    "data/resumes/raju_nalla_resume-DE.pdf"
)

skills = extractor.extract_skills(text)

print("=" * 60)
print("Extracted Skills")
print("=" * 60)

pprint(skills)

print("=" * 60)