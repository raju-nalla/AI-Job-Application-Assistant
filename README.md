# 🤖 AI Job Application Assistant

An enterprise-grade **AI-powered Job Application Assistant** that helps job seekers analyze resumes, evaluate ATS compatibility, optimize resumes, generate personalized cover letters, and prepare for interviews using Large Language Models (LLMs).

Built with a modular, production-ready architecture following **Software Development Life Cycle (SDLC)**, **Object-Oriented Programming (OOP)**, **Clean Code**, and **Agile Development** principles.

---

# 🚀 Features

## ✅ Resume Parsing

- Extracts text from PDF, DOCX, and TXT resumes
- Parses structured candidate information
- Supports multiple resume formats

---

## ✅ Job Description Parsing

- Reads TXT, PDF, and DOCX job descriptions
- Extracts job requirements
- Supports enterprise job descriptions

---

## ✅ Skill Extraction

- Centralized `skills.json`
- Skill alias detection
- Automatic skill normalization

Supports technologies including:

- Azure
- Azure Data Factory
- Azure Databricks
- Azure Synapse
- Snowflake
- Microsoft Fabric
- SQL
- Python
- PySpark
- SSIS
- Power BI
- Delta Lake
- and many more...

---

## ✅ ATS Matching Engine

- ATS Score Calculation
- Skill Matching
- Missing Skills Detection
- Extra Skills Analysis
- Category-wise ATS Scoring
- Improvement Recommendations

---

## ✅ ATS Report Generator

- Generates detailed ATS reports
- Markdown report generation
- Human-readable output
- Automatically saves reports

---

## ✅ Prompt Builder

- Dynamic prompt generation
- Placeholder replacement
- Centralized prompt management
- Reusable prompt templates

---

## ✅ AI Client

- OpenRouter Integration
- GPT OSS Support
- Retry mechanism
- Timeout handling
- Environment-based configuration
- Centralized logging

---

## ✅ Base AI Generator

Reusable AI framework powering every AI module.

Features:

- Prompt generation
- AI communication
- Markdown generation
- Report saving
- Shared logging
- Reusable architecture

---

## ✅ AI Resume Optimizer

- Generates ATS-optimized resumes
- Uses Resume + Job Description + ATS Report
- Improves ATS keyword alignment
- Preserves factual accuracy
- Markdown output

---

## ✅ AI Cover Letter Generator

- Generates personalized cover letters
- Tailored to target job descriptions
- Uses candidate resume
- ATS-friendly content
- Markdown output

---

## ✅ AI Interview Overview

Generates an interview preparation overview including:

- Candidate Summary
- ATS Strengths
- ATS Weaknesses
- Skills to Revise
- Company Overview
- Interview Strategy
- Final Preparation Tips

---

# 🚧 Upcoming Features

## Technical Interview Guide V2

- Beginner Technical Questions
- Intermediate Technical Questions
- Advanced Technical Questions
- Scenario-Based Questions
- Top Interview Questions
- Revision Concepts

---

## Behavioral Interview Guide V2

- Behavioral Questions
- HR Questions
- STAR Method Guidance
- Questions to Ask the Interviewer
- Company Research
- Final Interview Checklist

---

## Future Roadmap

- Report Manager
- Career Coach
- Resume Comparison
- Job Tracker
- Streamlit Web Application
- Docker Support
- GitHub Actions CI/CD

---

# 📁 Project Structure

```text
AI-Job-Application-Assistant/

│
├── config/
│   ├── __init__.py
│   ├── config_loader.py
│   └── settings.yaml
│
├── data/
│   ├── database/
│   ├── generated/
│   ├── job_descriptions/
│   ├── resumes/
│   ├── sample_outputs/
│   └── skills/
│       └── skills.json
│
├── logs/
│
├── modules/
│   ├── ai_client.py
│   ├── ats_engine.py
│   ├── ats_report_generator.py
│   ├── base_ai_generator.py
│   ├── cover_letter_generator.py
│   ├── database.py
│   ├── file_reader.py
│   ├── interview_overview.py
│   ├── job_description_parser.py
│   ├── logger.py
│   ├── prompt_builder.py
│   ├── resume_optimizer.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── technical_interview_guide.py
│   └── behavioral_interview_guide.py
│
├── prompts/
│   ├── resume/
│   │   └── resume_optimizer_prompt.txt
│   │
│   ├── cover_letter/
│   │   └── cover_letter_prompt.txt
│   │
│   └── interview/
│       ├── overview_prompt.txt
│       ├── beginner_prompt.txt
│       ├── intermediate_prompt.txt
│       ├── advanced_prompt.txt
│       ├── scenario_prompt.txt
│       ├── behavioral_prompt.txt
│       ├── hr_prompt.txt
│       └── top10_prompt.txt
│
├── reports/
│
├── tests/
│
├── tracker/
│
├── requirements.txt
├── README.md
├── .env.example
└── app.py
```

---

# ⚙️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.11+ |
| AI | OpenRouter |
| LLM | GPT OSS 20B Free |
| Configuration | YAML |
| Environment | python-dotenv |
| Database | SQLite |
| Parsing | pdfplumber, python-docx |
| Logging | Python Logging |
| Architecture | Modular + OOP |
| Development | SDLC + Agile |

---

# 🏗 Architecture

```text
                    Resume
                       │
                       ▼
                Resume Parser
                       │
                       ▼
               Skill Extractor
                       │
                       ▼
                ATS Matching Engine
                       │
                       ▼
              ATS Report Generator
                       │
                       ▼
                 ATS Analysis Report
                       │
                       ▼
                 Prompt Builder
                       │
                       ▼
              Base AI Generator
                       │
       ┌───────────────┼─────────────────┐
       ▼               ▼                 ▼
 Resume Optimizer  Cover Letter  Interview Overview
```

---

# ⚙️ Configuration

All application settings are managed through:

```text
config/settings.yaml
```

Example:

```yaml
ai:
  provider: openrouter
  model: openai/gpt-oss-20b:free
  timeout: 120
  max_completion_tokens: 4000
  max_retries: 3
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

# 🧪 Running Tests

Run individual modules:

```bash
python -m tests.test_logger
python -m tests.test_database
python -m tests.test_file_reader
python -m tests.test_resume_parser
python -m tests.test_job_description_parser
python -m tests.test_skill_extractor
python -m tests.test_ats_engine
python -m tests.test_ats_report_generator
python -m tests.test_prompt_builder
python -m tests.test_resume_optimizer
python -m tests.test_cover_letter_generator
python -m tests.test_interview_overview
python -m tests.test_technical_interview
```

Run the complete pipeline:

```bash
python -m tests.test_resume_pipeline
```

---

# 📈 Current Progress

| Sprint | Status |
|----------|--------|
| Sprint 1 | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 3 | ✅ Completed |
| Sprint 4 | ✅ Completed |
| Sprint 5 | ✅ Completed |
| Sprint 6 | ✅ Completed |
| Sprint 7 | 🚧 In Progress |

### Sprint 7 Deliverables

- ✅ Base AI Generator
- ✅ AI Resume Optimizer
- ✅ AI Cover Letter Generator
- ✅ AI Interview Overview
- 🚧 Technical Interview Guide V2
- 🚧 Behavioral Interview Guide V2
- 🚧 Prompt Architecture Refactoring

---

# 🎯 Project Goals

- Improve ATS compatibility using AI
- Automate resume optimization
- Generate personalized cover letters
- Prepare candidates for technical interviews
- Generate behavioral interview preparation
- Provide AI-powered career guidance
- Track job applications
- Build a complete AI Job Application Assistant

---

# 👨‍💻 Author

**Raju Nalla**

**Azure Data Engineer**

- **GitHub:** https://github.com/raju-nalla
- **Portfolio:** https://raju-nalla.github.io/
- **LinkedIn:** https://www.linkedin.com/in/raju-nalla

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

# 📌 Project Status

🚀 **Current Version:** v1.1.0

This project is actively being developed.

### Completed

- Resume Parser
- Job Description Parser
- Skill Extraction Engine
- ATS Matching Engine
- ATS Report Generator
- AI Resume Optimizer
- AI Cover Letter Generator
- AI Interview Overview
- Base AI Generator Framework

### In Progress

- Technical Interview Guide V2
- Behavioral Interview Guide V2
- Multi-stage AI Generation Architecture

### Planned

- Report Manager
- Career Coach
- Resume Comparison
- Job Tracker
- Streamlit Dashboard
- Docker Deployment
- GitHub Actions CI/CD
- Multi-Model AI Support