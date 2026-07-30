# 🤖 AI Job Application Assistant

An enterprise-grade AI-powered application that helps job seekers optimize resumes, improve ATS scores, generate cover letters, and prepare for interviews using Large Language Models (LLMs).

Built with a modular, production-ready architecture following Software Development Life Cycle (SDLC) and Agile methodologies.

---

## 🚀 Features

### ✅ Resume Parsing
- Extracts text from PDF and DOCX resumes
- Structured resume processing

### ✅ Job Description Parsing
- Reads and analyzes job descriptions
- Extracts required skills and technologies

### ✅ Skill Extraction
- Detects technical skills using configurable skill dictionaries
- Supports Azure, Snowflake, Databricks, Python, SQL, Spark, and more

### ✅ ATS Score Engine
- Calculates ATS compatibility score
- Skill matching analysis
- Missing skills identification
- Category-wise scoring
- Recommendations for improvement

### ✅ ATS Report Generator
- Generates detailed ATS reports
- Highlights strengths and weaknesses
- Saves reports locally

### ✅ Prompt Builder
- Uses reusable prompt templates
- Dynamic placeholder replacement
- Easy prompt customization

### ✅ AI Client
- Centralized AI integration
- OpenRouter support
- Configurable LLM model
- Retry mechanism
- Logging
- Environment-based configuration

---

## 🚧 Upcoming Features

- AI Resume Optimizer
- Cover Letter Generator
- Interview Question Generator
- Career Coach
- Job Tracker
- Streamlit Web Application
- Recruiter Dashboard

---

# 📁 Project Structure

```text
AI-Job-Application-Assistant/

│
├── config/
│   ├── settings.yaml
│   └── config_loader.py
│
├── data/
│   ├── database/
│   ├── generated/
│   └── samples/
│
├── modules/
│   ├── logger.py
│   ├── database.py
│   ├── file_reader.py
│   ├── resume_parser.py
│   ├── job_description_parser.py
│   ├── skill_extractor.py
│   ├── ats_engine.py
│   ├── ats_report_generator.py
│   ├── prompt_builder.py
│   └── openai_client.py
│
├── prompts/
│   ├── resume_optimizer_prompt.txt
│   ├── cover_letter_prompt.txt
│   ├── interview_prompt.txt
│   └── career_coach_prompt.txt
│
├── reports/
│
├── tracker/
│
├── tests/
│
├── logs/
│
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.11+ |
| AI | OpenRouter |
| LLM | GPT OSS 20B Free |
| Configuration | YAML |
| Environment | dotenv |
| Database | SQLite |
| Parsing | PyPDF2, python-docx |
| Logging | Python Logging |
| Architecture | Modular |
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
ATS Engine
      │
      ▼
ATS Report
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
Optimized Resume
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
  timeout: 60
  max_completion_tokens: 2000
  max_retries: 3
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

> If using OpenRouter, store your OpenRouter API key and configure the client accordingly.

---

# 🧪 Running Tests

```bash
python test_logger.py

python test_database.py

python test_file_reader.py

python test_resume_parser.py

python test_job_description_parser.py

python test_ats_engine.py

python test_ats_report_generator.py

python test_config_loader.py

python test_prompt_builder.py

python test_openai_client.py
```

---

# 📈 Current Progress

| Sprint | Status |
|----------|--------|
| Sprint 1 | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 3 | ✅ Completed |
| Sprint 4 | ✅ Completed |
| Sprint 5 | 🚧 In Progress |

Completed in Sprint 5:

- Prompt Templates
- Prompt Builder
- Configuration Loader
- AI Client (OpenRouter)

Upcoming:

- Resume Optimizer
- Cover Letter Generator
- Interview Coach

---

# 🎯 Project Goals

- Improve ATS scores using AI
- Automate resume customization
- Generate personalized cover letters
- Prepare candidates for interviews
- Provide career guidance
- Track job applications

---

# 👨‍💻 Author

**Raju Nalla**

Azure Data Engineer

GitHub: https://github.com/raju-nalla

Portfolio: https://raju-nalla.github.io/

LinkedIn: https://www.linkedin.com/in/raju-nalla

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.