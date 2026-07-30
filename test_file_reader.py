from modules.file_reader import FileReader

reader = FileReader()

text = reader.read("data/resumes/raju_nalla_resume-DE.pdf")

print("=" * 60)
print(text[:1000])     # Print first 1000 characters
print("=" * 60)