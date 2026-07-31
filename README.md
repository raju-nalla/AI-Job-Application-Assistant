# 🤖 AI Job Application Assistant

An enterprise-grade AI-powered application that helps job seekers analyze resumes, evaluate ATS compatibility, optimize resumes using Large Language Models (LLMs), and automate the job application process.

Built using a modular, production-ready architecture following Software Development Life Cycle (SDLC), Clean Code principles, and Agile methodologies.

---

# 🚀 Features

## ✅ Resume Parsing
- Extracts text from PDF, DOCX, and TXT resumes
- Parses candidate information
- Returns structured resume data

---

## ✅ Job Description Parsing
- Reads job descriptions from TXT, PDF, and DOCX
- Extracts job title, company, and experience
- Returns structured job description data

---

## ✅ Skill Extraction
- Detects technical skills using a centralized `skills.json`
- Supports aliases for accurate matching
- Configurable skill repository
- Supports Azure, Snowflake, Databricks, PySpark, SQL, Python, SSIS, Power BI, and more

---

## ✅ ATS Matching Engine
- Calculates Overall ATS Score
- Category-wise scoring
- Skill matching analysis
- Missing skills identification
- Extra skills detection
- Strength & weakness analysis
- Intelligent recommendations

---

## ✅ ATS Report Generator
- Generates formatted ATS reports
- Displays strengths and weaknesses
- Highlights missing skills
- Saves reports automatically

---

## ✅ Prompt Builder
- Uses reusable prompt templates
- Dynamic placeholder replacement
- Centralized prompt management

---

## ✅ AI Client
- OpenRouter API integration
- Configurable LLM model
- Retry mechanism
- Timeout handling
- Centralized logging
- Environment-based configuration

---

## ✅ AI Resume Optimizer
- Generates ATS-optimized resumes using LLMs
- Uses Resume + Job Description + ATS Report
- Preserves factual accuracy
- Improves resume wording for ATS compatibility
- Saves optimized resume in Markdown format

---

## ✅ AI Cover Letter Generator
- Generates personalized cover letters using AI
- Tailors content to the job description
- Uses candidate resume for personalization
- Preserves factual accuracy
- Saves output in Markdown format

---

# 🚧 Upcoming Features

- Interview Question Generator
- Interview Answer Evaluator
- Career Coach
- Resume Comparison
- Job Tracker
- Streamlit Web Application
- Recruiter Dashboard

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
│   ├── database.py
│   ├── file_reader.py
│   ├── job_description_parser.py
│   ├── logger.py
│   ├── prompt_builder.py
│   ├── resume_optimizer.py
|   ├── cover_letter_generator.py
│   ├── resume_parser.py
│   └── skill_extractor.py
│
├── prompts/
│   ├── resume_optimizer_prompt.txt
│   ├── cover_letter_prompt.txt
│   ├── interview_prompt.txt
│   └── career_coach_prompt.txt
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
| LLM | GPT-OSS-20B |
| Configuration | YAML |
| Environment | python-dotenv |
| Database | SQLite |
| Parsing | pdfplumber, python-docx |
| Logging | Python Logging |
| Architecture | Modular |
| Development | SDLC + Agile |

---

# 🏗️ Architecture

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
         Resume Skills Dictionary
                   │
                   │
Job Description ───┘
       │
       ▼
Job Description Parser
       │
       ▼
Skill Extractor
       │
       ▼
JD Skills Dictionary
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
            AI Client
               │
               ▼
      Large Language Model
               │
               ▼
     Optimized Resume (.md)
```

---

# ⚙️ Configuration

Application settings are managed through:

```text
config/settings.yaml
```

Example:

```yaml
ai:
  provider: openrouter
  model: openai/gpt-oss-20b:free
  timeout: 60
  max_completion_tokens: 2000
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

Run individual module tests:

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
python -m test_cover_letter_generator.py
```

Run the complete end-to-end pipeline:

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
| Sprint 6 | 🚧 In Progress |

|----------|--------|
| Sprint 1 | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 3 | ✅ Completed |
| Sprint 4 | ✅ Completed |
| Sprint 5 | ✅ Completed |

### Sprint 6 Deliverables

- ✅ AI Cover Letter Generator
- ⏳ Interview Question Generator
- ⏳ Interview Answer Evaluator
- ⏳ Career Coach
- ⏳ Resume Comparison

---

# 🎯 Project Goals

- Improve ATS scores using AI
- Automate resume optimization
- Generate personalized cover letters
- Prepare candidates for interviews
- Provide AI-powered career guidance
- Track job applications
- Build a complete AI Job Application Assistant

---

# 👨‍💻 Author

**Raju Nalla**

Azure Data Engineer

- GitHub: https://github.com/raju-nalla
- Portfolio: https://raju-nalla.github.io/
- LinkedIn: https://www.linkedin.com/in/raju-nalla

---

# ⭐ Support

If you found this project useful, please consider giving the repository a ⭐ on GitHub.