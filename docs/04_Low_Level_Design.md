# Low Level Design (LLD)

# AI Job Application Assistant

**Version:** 1.0  
**Author:** Raju Nalla  
**Sprint:** 2  
**Document Type:** Low Level Design (LLD)

---

# 1. Introduction

## 1.1 Purpose

This Low-Level Design (LLD) document defines the implementation details of the AI Job Application Assistant. It describes the project structure, modules, classes, functions, file organization, configuration, logging, exception handling, and interaction between components.

---

# 2. Project Structure

```
AI-Job-Application-Assistant/

│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   └── settings.yaml
│
├── data/
│   ├── resumes/
│   ├── job_descriptions/
│   ├── generated/
│   └── database/
│
├── docs/
│
├── logs/
│
├── modules/
│   ├── ats_engine.py
│   ├── jd_parser.py
│   ├── resume_parser.py
│   ├── resume_generator.py
│   ├── cover_letter.py
│   ├── tracker.py
│   ├── dashboard.py
│   └── database.py
│
├── prompts/
│
├── templates/
│
├── tests/
│
└── reports/
```

---

# 3. Module Design

## Module 1 – Job Description Parser

### Purpose

Extract structured information from Job Descriptions.

### Inputs

- PDF
- DOCX
- TXT

### Outputs

```python
{
    "company": "",
    "job_title": "",
    "experience": "",
    "skills": [],
    "responsibilities": [],
    "education": []
}
```

Functions

```
load_file()

extract_text()

extract_skills()

extract_keywords()

parse_job_description()
```

---

## Module 2 – Resume Parser

Purpose

Extract structured resume information.

Output

```
Name

Skills

Projects

Education

Experience

Certifications
```

Functions

```
load_resume()

extract_sections()

extract_skills()

extract_projects()

parse_resume()
```

---

## Module 3 – ATS Engine

Purpose

Compare Resume with Job Description.

Functions

```
calculate_match()

find_missing_skills()

calculate_keyword_score()

generate_recommendations()
```

Output

```
ATS Score

Missing Skills

Recommendations
```

---

## Module 4 – Resume Generator

Purpose

Generate ATS optimized resume.

Functions

```
optimize_resume()

generate_docx()

generate_pdf()
```

---

## Module 5 – Cover Letter Generator

Functions

```
generate_cover_letter()

generate_recruiter_email()

generate_linkedin_message()
```

---

## Module 6 – Application Tracker

Functions

```
save_application()

update_status()

get_statistics()

delete_application()
```

---

## Module 7 – Dashboard

Functions

```
load_dashboard()

application_summary()

ats_statistics()

skills_gap_chart()
```

---

# 4. User Interface Flow

```
Home

↓

Upload Resume

↓

Upload Job Description

↓

ATS Analysis

↓

Resume Optimization

↓

Cover Letter

↓

Application Tracker

↓

Dashboard
```

---

# 5. Database Interaction

```
UI

↓

Business Logic

↓

SQLite

↓

Application Data
```

---

# 6. Configuration

Configuration file

```
config/settings.yaml
```

Example

```yaml
app_name: AI Job Application Assistant

database: data/database/job_tracker.db

log_level: INFO

output_directory: data/generated
```

---

# 7. Logging

Log file

```
logs/application.log
```

Log Levels

```
INFO

WARNING

ERROR

DEBUG
```

Logged Events

- Application Start
- Resume Upload
- JD Upload
- ATS Calculation
- Resume Generation
- AI Requests
- Exceptions

---

# 8. Exception Handling

Common Exceptions

```
FileNotFoundError

Invalid PDF

Invalid DOCX

DatabaseError

APIError

TimeoutError
```

Handling Strategy

- Display user-friendly messages.
- Write detailed errors to logs.
- Continue execution where possible.

---

# 9. Validation Rules

Resume

- PDF
- DOCX
- Maximum 10 MB

Job Description

- PDF
- DOCX
- TXT

Required

- Resume
- Job Description

---

# 10. File Storage

```
data/

resumes/

job_descriptions/

generated/

database/
```

Generated Files

```
Resume.docx

Resume.pdf

CoverLetter.docx

CoverLetter.pdf
```

---

# 11. Coding Standards

Python Style Guide

- PEP 8
- Type Hints
- Docstrings
- Modular Functions
- Meaningful Variable Names

Naming Convention

```
snake_case

PascalCase (Classes)

UPPER_CASE (Constants)
```

---

# 12. Testing Strategy

Unit Testing

- Parser Tests
- ATS Tests
- Database Tests
- Resume Generator Tests

Integration Testing

- End-to-End Workflow

Tools

- pytest

---

# 13. Future Refactoring

After MVP completion, the project structure may be migrated to a service-based architecture:

```
src/
├── ai/
├── database/
├── parsers/
├── services/
├── utils/
└── config/
```

This refactoring will improve maintainability and support future enhancements such as cloud deployment, REST APIs, and AI agents.

---

# 14. Sequence Flow

```
User

↓

Upload Resume

↓

Resume Parser

↓

Upload Job Description

↓

JD Parser

↓

ATS Engine

↓

Resume Generator

↓

Cover Letter Generator

↓

Save Application

↓

Dashboard
```

---

# 15. Conclusion

The Low-Level Design provides the implementation blueprint for the AI Job Application Assistant. It defines the internal structure, module responsibilities, function-level design, coding standards, and interaction between components. The design follows modular programming principles to simplify development, testing, and future enhancements while keeping the initial MVP implementation straightforward.