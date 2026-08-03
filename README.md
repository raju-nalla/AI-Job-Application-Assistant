# 🤖 AI Job Application Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-orange?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Powered-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

### 🚀 Enterprise AI-Powered Resume Optimization & Interview Preparation Platform

**Analyze • Optimize • Prepare • Succeed**

</div>

---

# 📖 Overview

AI Job Application Assistant is an enterprise-grade AI application that helps job seekers optimize their resumes, improve ATS compatibility, generate personalized cover letters, and prepare for technical and behavioral interviews using Large Language Models (LLMs).

The application combines traditional resume parsing and ATS analysis with AI-powered content generation to create a complete job application preparation workflow.

Built using modern software engineering practices, the project follows:

- Object-Oriented Programming (OOP)
- SOLID Design Principles
- Modular Architecture
- Clean Code
- SDLC Best Practices
- Agile Development
- AI-Driven Automation

---

# 🎯 Project Objectives

The primary goal of this project is to automate the entire job application preparation process.

Instead of manually editing resumes and preparing for interviews, candidates can generate professional application materials in minutes.

The application provides:

- Resume Analysis
- ATS Compatibility Analysis
- Resume Optimization
- Personalized Cover Letter Generation
- Technical Interview Preparation
- Behavioral Interview Preparation
- HR Interview Preparation
- Company Research
- Interview Strategy Guidance

---

# ✨ Features

## 📄 Resume Parsing

- Parse PDF resumes
- Parse DOCX resumes
- Parse TXT resumes
- Extract structured candidate information
- Support multiple resume formats
- Enterprise-ready parser

---

## 📋 Job Description Parsing

- Parse TXT Job Descriptions
- Parse PDF Job Descriptions
- Parse DOCX Job Descriptions
- Extract required skills
- Extract experience requirements
- Enterprise job description support

---

## 🧠 Skill Extraction Engine

Automatically extracts technical skills using a centralized skills database.

Supported technologies include:

### Cloud Platforms

- Microsoft Azure
- Microsoft Fabric
- Snowflake

### Data Engineering

- Azure Data Factory
- Azure Databricks
- Azure Synapse
- Delta Lake
- Data Warehousing
- ETL
- ELT

### Programming

- Python
- PySpark
- SQL
- T-SQL

### Databases

- SQL Server
- Oracle
- PostgreSQL
- Snowflake

### BI & Analytics

- Power BI
- SSIS

---

## 📊 ATS Matching Engine

Automatically compares the candidate's resume against the target Job Description.

Features include:

- ATS Score Calculation
- Skill Matching
- Missing Skill Detection
- Extra Skill Identification
- Resume Gap Analysis
- ATS Improvement Recommendations

---

## 📑 ATS Report Generation

Automatically generates a detailed ATS report including:

- Overall ATS Score
- Matching Skills
- Missing Skills
- Resume Strengths
- Resume Weaknesses
- Improvement Suggestions

Generated as a Markdown report.

---

## 🤖 AI Resume Optimizer

Uses Large Language Models (LLMs) to:

- Optimize Resume
- Improve ATS Compatibility
- Enhance Resume Content
- Improve Technical Bullet Points
- Preserve Resume Accuracy
- Maintain Professional Formatting

---

## ✉️ AI Cover Letter Generator

Generates personalized cover letters using:

- Candidate Resume
- Job Description
- ATS Analysis

Each cover letter is tailored specifically for the target role.

---

## 🎯 Interview Overview Generator

Generates a complete interview preparation overview including:

- Candidate Profile Summary
- ATS Analysis Summary
- Technical Strengths
- Areas for Improvement
- Interview Preparation Strategy
- Final Recommendations

---

## 💻 Technical Interview Guide

Generates AI-powered technical interview preparation including:

- Beginner Questions
- Intermediate Questions
- Advanced Questions
- Scenario-Based Questions
- Top Interview Questions

Focused on modern Data Engineering technologies such as:

- Azure
- Azure Data Factory
- Azure Databricks
- Snowflake
- Microsoft Fabric
- SQL
- Python
- PySpark
- Delta Lake

---

## 👥 Behavioral Interview Guide

Generates complete behavioral interview preparation including:

- Behavioral Questions
- HR Questions
- STAR Method Answers
- Company Research
- Questions to Ask the Interviewer
- Interview Checklist

---

## 🧩 Prompt Builder

A centralized prompt management system that provides:

- Dynamic Prompt Loading
- Placeholder Replacement
- Prompt Validation
- Template Reusability
- Shared Prompt Architecture

---

## 🌐 OpenRouter AI Integration

Supports AI generation using OpenRouter.

Current configuration includes:

- GPT OSS Models
- Configurable Timeout
- Retry Mechanism
- Environment Variables
- Centralized AI Client
- Shared AI Framework

---

# 🏗 Architecture

```text
                          Resume
                             │
                             ▼
                     Resume Parser
                             │
                             ▼
                    Resume Cleaner
                             │
                             ▼
                  Job Description Parser
                             │
                             ▼
                 Job Description Cleaner
                             │
                             ▼
                    Skill Extraction
                             │
                             ▼
                     ATS Matching Engine
                             │
                             ▼
                    ATS Report Generator
                             │
                             ▼
                  Prompt Context Builder
                             │
                             ▼
                     Prompt Builder
                             │
                             ▼
                     Base AI Generator
                             │
     ┌───────────────┼────────────────┬────────────────┐
     ▼               ▼                ▼                ▼
Resume          Cover Letter    Interview       Technical &
Optimizer         Generator      Overview      Behavioral Guides
```

---

# 🚀 End-to-End Workflow

```text
Resume
   │
   ▼
Resume Parsing
   │
   ▼
Resume Cleaning
   │
   ▼
Job Description Parsing
   │
   ▼
Job Description Cleaning
   │
   ▼
Skill Extraction
   │
   ▼
ATS Comparison
   │
   ▼
ATS Report
   │
   ▼
Prompt Context Builder
   │
   ▼
AI Report Generation
   │
   ├──────── Resume Optimizer
   ├──────── Cover Letter
   ├──────── Interview Overview
   ├──────── Technical Interview Guide
   └──────── Behavioral Interview Guide
```

---

# 🌟 Key Highlights

- ✅ Enterprise Architecture
- ✅ Modular Design
- ✅ Object-Oriented Programming
- ✅ AI-Powered Automation
- ✅ ATS Resume Optimization
- ✅ OpenRouter Integration
- ✅ Markdown Report Generation
- ✅ Configurable Prompt System
- ✅ Production-Ready Logging
- ✅ Extensible AI Framework

# 📂 Project Structure

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
│   ├── behavioral_interview_guide.py
│   ├── cover_letter_generator.py
│   ├── database.py
│   ├── file_reader.py
│   ├── interview_overview.py
│   ├── job_description_cleaner.py
│   ├── job_description_parser.py
│   ├── logger.py
│   ├── prompt_builder.py
│   ├── prompt_context_builder.py
│   ├── report_manager.py
│   ├── resume_cleaner.py
│   ├── resume_optimizer.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── technical_interview_guide.py
│   └── workflow_builder.py
│
├── prompts/
│   ├── behavioral/
│   ├── cover_letter/
│   ├── interview/
│   └── resume/
│
├── reports/
│
├── tests/
│
├── tracker/
│
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙ Technology Stack

| Category | Technology |
|------------|------------|
| Programming Language | Python 3.12 |
| AI Provider | OpenRouter |
| LLM | GPT OSS 20B |
| Resume Parsing | pdfplumber |
| DOCX Parsing | python-docx |
| Configuration | YAML |
| Environment Variables | python-dotenv |
| Database | SQLite |
| Logging | Python Logging |
| Output Format | Markdown |
| Architecture | OOP + Modular |
| Development | SDLC + Agile |

---

# 💻 System Requirements

Minimum Requirements

- Python 3.11 or above
- Git
- OpenRouter API Key
- Internet Connection

Recommended

- Python 3.12
- Visual Studio Code
- Windows / Linux / macOS

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/raju-nalla/AI-Job-Application-Assistant.git
```

Move into the project directory

```bash
cd AI-Job-Application-Assistant
```

Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Example

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# ⚙ Configuration

All application settings are managed from:

```text
config/settings.yaml
```

Example

```yaml
ai:
  provider: openrouter
  model: openai/gpt-oss-20b:free
  timeout: 300
  max_completion_tokens: 4000
  max_retries: 3

paths:
  resume: data/resumes/raju_nalla_resume-DE.pdf
  job_description: data/job_descriptions/senior_data_engineer_ssis.txt
  prompts: prompts
  reports: reports
```

---

# 📄 Supported Input Files

## Resume

Supported formats

- PDF
- DOCX
- TXT

Example

```text
data/resumes/raju_nalla_resume-DE.pdf
```

---

## Job Description

Supported formats

- TXT
- PDF
- DOCX

Example

```text
data/job_descriptions/senior_data_engineer_ssis.txt
```

---

# ▶ Running the Application

Simply execute

```bash
python main.py
```

The application automatically performs:

1. Resume Parsing
2. Resume Cleaning
3. Job Description Parsing
4. Job Description Cleaning
5. Skill Extraction
6. ATS Analysis
7. ATS Report Generation
8. Resume Optimization
9. Cover Letter Generation
10. Interview Overview Generation
11. Technical Interview Guide Generation
12. Behavioral Interview Guide Generation

---

# 📊 Generated Reports

All generated reports are saved inside:

```text
reports/
```

Generated files include

```text
reports/
│
├── ats_report.md
├── optimized_resume.md
├── cover_letter.md
├── interview_overview.md
├── technical_interview_guide.md
└── behavioral_interview_guide.md
```

---

# 📝 Sample Console Output

```text
============================================================
 AI JOB APPLICATION ASSISTANT
============================================================

✓ Resume Optimizer Generated

✓ Cover Letter Generated

✓ Interview Overview Generated

✓ Technical Interview Guide Generated

✓ Behavioral Interview Guide Generated

------------------------------------------------------------

Reports Folder : reports/

Execution Time : 610 sec

============================================================
```

---

# 🧪 Running Tests

Run individual modules

```bash
python -m tests.test_logger
```

```bash
python -m tests.test_resume_parser
```

```bash
python -m tests.test_job_description_parser
```

```bash
python -m tests.test_skill_extractor
```

```bash
python -m tests.test_ats_engine
```

```bash
python -m tests.test_ats_report_generator
```

```bash
python -m tests.test_prompt_builder
```

```bash
python -m tests.test_resume_optimizer
```

```bash
python -m tests.test_cover_letter_generator
```

```bash
python -m tests.test_interview_overview
```

```bash
python -m tests.test_technical_interview
```

Run the complete application

```bash
python main.py
```

---

# 📈 Performance

Typical execution time

| Module | Average Time |
|----------|-------------:|
| Resume Parsing | 1 sec |
| ATS Analysis | <1 sec |
| Resume Optimization | 2–3 min |
| Cover Letter | 1 min |
| Interview Overview | 1 min |
| Technical Guide | 3–4 min |
| Behavioral Guide | 3–4 min |
| Total | ~10 min |

Execution time depends on:

- AI Model
- Internet Speed
- Prompt Size
- OpenRouter Response Time

---

---

# 🛣️ Roadmap

## ✅ Version 1.0 (Current)

Completed Features

- [x] Resume Parser
- [x] Resume Cleaner
- [x] Job Description Parser
- [x] Job Description Cleaner
- [x] Skill Extraction Engine
- [x] ATS Matching Engine
- [x] ATS Report Generator
- [x] Prompt Context Builder
- [x] Prompt Builder
- [x] OpenRouter AI Integration
- [x] AI Resume Optimizer
- [x] AI Cover Letter Generator
- [x] AI Interview Overview
- [x] Technical Interview Guide
- [x] Behavioral Interview Guide
- [x] Markdown Report Generation
- [x] Enterprise Logging
- [x] Configuration Management

---

## 🚀 Version 2.0 (Planned)

### AI Enhancements

- [ ] Multi-Model AI Support
- [ ] Azure OpenAI Support
- [ ] Google Gemini Support
- [ ] Anthropic Claude Support
- [ ] OpenAI GPT Support
- [ ] AI Response Caching
- [ ] Automatic Retry with Fallback Models

---

### Report Enhancements

- [ ] PDF Resume Generation
- [ ] DOCX Resume Generation
- [ ] DOCX Cover Letter
- [ ] PDF Cover Letter
- [ ] PowerPoint Interview Notes
- [ ] Excel ATS Report
- [ ] HTML Reports

---

### User Interface

- [ ] Streamlit Dashboard
- [ ] Gradio Interface
- [ ] Drag & Drop Resume Upload
- [ ] Job Description Paste Window
- [ ] Progress Bar
- [ ] Dark Mode
- [ ] Download Center

---

### Performance

- [ ] Parallel AI Generation
- [ ] Async Processing
- [ ] Multi-threaded Report Generation
- [ ] Faster Resume Parsing
- [ ] Intelligent Prompt Optimization

---

### Cloud Features

- [ ] Docker Support
- [ ] GitHub Actions
- [ ] Azure Deployment
- [ ] AWS Deployment
- [ ] CI/CD Pipeline

---

# 📊 Development Workflow

```text
                Candidate Resume
                        │
                        ▼
               Resume Parsing Module
                        │
                        ▼
               Resume Cleaning Module
                        │
                        ▼
          Job Description Parsing Module
                        │
                        ▼
          Job Description Cleaning Module
                        │
                        ▼
              Skill Extraction Engine
                        │
                        ▼
                 ATS Matching Engine
                        │
                        ▼
              ATS Report Generation
                        │
                        ▼
             Prompt Context Builder
                        │
                        ▼
                Prompt Builder
                        │
                        ▼
                 Base AI Generator
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Resume Optimizer  Cover Letter   Interview Guides
                                         │
                           ┌─────────────┴────────────┐
                           ▼                          ▼
                  Technical Guide          Behavioral Guide
```

---

# 🧠 Design Principles

This project follows modern software engineering practices.

- Object-Oriented Programming (OOP)
- SOLID Principles
- Separation of Concerns
- Modular Architecture
- Reusable Components
- DRY (Don't Repeat Yourself)
- Clean Code Practices
- Configuration-Driven Design
- AI Prompt Engineering
- Enterprise Logging

---

# 🔒 Security

Sensitive information is never stored in source code.

Use environment variables for:

- OpenRouter API Key
- Azure Keys
- Future AI Providers

Never commit:

```text
.env
*.log
__pycache__/
```

---

# 🤝 Contributing

Contributions are welcome.

### Steps

Fork the repository.

```bash
git clone https://github.com/<your-username>/AI-Job-Application-Assistant.git
```

Create a feature branch.

```bash
git checkout -b feature/new-feature
```

Commit your changes.

```bash
git commit -m "Add new feature"
```

Push the branch.

```bash
git push origin feature/new-feature
```

Create a Pull Request.

---

# 🐞 Reporting Issues

If you encounter any bugs:

1. Check existing Issues.
2. Create a new Issue.
3. Include:
   - Python Version
   - Operating System
   - Error Logs
   - Steps to Reproduce

---

# 📚 Learning Objectives

This project demonstrates practical implementation of:

- Python Programming
- Object-Oriented Design
- AI Prompt Engineering
- Resume Parsing
- ATS Optimization
- Enterprise Logging
- Configuration Management
- OpenRouter Integration
- Large Language Models (LLMs)
- Modular Software Development

---

# 👨‍💻 Author

**Raju Nalla**

Azure Data Engineer | AI Enthusiast | Data Engineering Professional

### Connect with me

- LinkedIn: https://www.linkedin.com/in/raju-nalla
- GitHub: https://github.com/raju-nalla

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and extend this project for learning and personal use.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🛠 Contribute improvements

📢 Share with the community

---

# 🙏 Acknowledgements

Special thanks to:

- OpenRouter
- OpenAI
- Python Community
- Open Source Contributors

---

# 🎯 Project Status

```text
Version        : 1.0.0

Status         : Stable

Architecture   : Enterprise Modular Design

AI Provider    : OpenRouter

Language       : Python 3.12

Reports        : Markdown

Current Phase  : Production Ready

Next Phase     : Web Application (Version 2.0)
```

---

<div align="center">

# ⭐ Thank You ⭐

### AI Job Application Assistant

**Analyze • Optimize • Prepare • Succeed**

Made with ❤️ using Python & AI

</div>