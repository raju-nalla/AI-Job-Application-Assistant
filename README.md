# 🚀 AI Job Application Assistant

An enterprise-grade AI-powered application that automates the job application lifecycle, including resume parsing, job description parsing, ATS compatibility analysis, resume optimization, cover letter generation, and application tracking.

The project is built using **Python**, **Streamlit**, **SQLite**, and **OpenAI**, following **Software Development Life Cycle (SDLC)** and **Agile Scrum** methodologies.

---

# 📌 Project Overview

The AI Job Application Assistant helps job seekers streamline their application process by:

- 📄 Parse resumes (PDF, DOCX, TXT)
- 📄 Parse job descriptions
- 🧠 Extract technical skills intelligently
- 🎯 Perform enterprise-grade ATS analysis
- 📊 Generate ATS analysis reports
- 📝 Optimize resumes using AI *(Upcoming)*
- ✉️ Generate AI-powered cover letters *(Upcoming)*
- 📈 Track job applications *(Upcoming)*

The project emphasizes:

- Enterprise Software Design
- Modular Architecture
- Object-Oriented Programming
- Clean Code
- Reusable Components
- Agile Sprint-Based Development

---

# ✅ Current Features

### Core Modules

- ✅ Centralized Logging Framework
- ✅ SQLite Database Management
- ✅ PDF / DOCX / TXT File Reader
- ✅ Resume Parser
- ✅ Job Description Parser
- ✅ Enterprise Skill Repository
- ✅ Intelligent Skill Extractor
- ✅ Enterprise ATS Matching Engine
- ✅ ATS Report Generator

---

# 🏗 Architecture

```text
                          Streamlit UI
                               │
                               ▼
                     Business Logic Layer
                               │
     ┌───────────────┬───────────────┬───────────────┐
     ▼               ▼               ▼
 Resume Parser   JD Parser   ATS Report Generator
     │               │               ▲
     ▼               ▼               │
 Skill Extractor ───────► ATS Engine
     │
     ▼
 Skills Repository (skills.json)
                               │
                               ▼
                        SQLite Database
```

---

# 📁 Project Structure

```text
AI-Job-Application-Assistant/

│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│
├── data/
│   ├── database/
│   ├── generated/
│   ├── job_descriptions/
│   ├── resumes/
│   └── skills/
│       └── skills.json
│
├── docs/
│
├── logs/
│   └── application.log
│
├── modules/
│   ├── logger.py
│   ├── database.py
│   ├── file_reader.py
│   ├── resume_parser.py
│   ├── job_description_parser.py
│   ├── skill_extractor.py
│   ├── ats_engine.py
│   └── ats_report_generator.py
│
├── prompts/
├── reports/
├── templates/
├── tests/
└── tracker/
```

---

# 🚀 Enterprise Workflow

```text
Resume
   │
   ▼
File Reader
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
ATS Report Generator
   │
   ▼
ATS Analysis Report
```

---

# ✨ ATS Engine Features

The Enterprise ATS Engine provides:

- ✅ Weighted ATS Score
- ✅ Category-wise Skill Matching
- ✅ Priority-based Skill Analysis
- ✅ Missing Skill Detection
- ✅ Extra Skill Identification
- ✅ Strength Analysis
- ✅ Weakness Analysis
- ✅ Intelligent Recommendations
- ✅ Professional ATS Report Generation

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| UI | Streamlit |
| Database | SQLite |
| AI | OpenAI API *(Upcoming)* |
| Data Processing | Pandas |
| Document Processing | pdfplumber, python-docx |
| Visualization | Plotly |
| Version Control | Git & GitHub |

---

# 📂 Project Documentation

| Document | Status |
|----------|--------|
| Project Charter | ✅ |
| Software Requirements Specification | ✅ |
| High-Level Design | ✅ |
| Low-Level Design | ✅ |
| Database Design | ✅ |
| UI Wireframes | ✅ |
| Sprint Backlog | ✅ |
| Project Roadmap | ✅ |

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/raju-nalla/AI-Job-Application-Assistant.git
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 📅 Development Roadmap

| Sprint | Deliverable | Status |
|---------|-------------|--------|
| Sprint 1 | Project Setup | ✅ Completed |
| Sprint 2 | Architecture & Design | ✅ Completed |
| Sprint 3 | Resume & JD Parsing Modules | ✅ Completed |
| Sprint 4 | Enterprise ATS Analysis Engine | ✅ Completed |
| Sprint 5 | AI Resume Optimizer | 🚧 In Progress |
| Sprint 6 | AI Cover Letter Generator | ⏳ Planned |
| Sprint 7 | Streamlit Dashboard | ⏳ Planned |
| Sprint 8 | Deployment | ⏳ Planned |

---

# 🎯 Future Enhancements

- AI Resume Optimizer
- AI Cover Letter Generator
- AI Career Coach
- Interview Preparation Assistant
- Resume Version Management
- Job Recommendation Engine
- PostgreSQL Support
- FastAPI REST APIs
- Azure Cloud Deployment
- User Authentication
- Multi-user Support
- Email Automation

---

# 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Raju Nalla**

**Azure Data Engineer | Python Developer | Data Engineering Enthusiast**

- GitHub: https://github.com/raju-nalla
- LinkedIn: https://www.linkedin.com/in/raju-nalla

---

# ⭐ Project Status

## 🚀 Active Development

### Completed

- ✅ Sprint 1 – Project Setup
- ✅ Sprint 2 – Software Design & Architecture
- ✅ Sprint 3 – Resume & Job Description Parsing
- ✅ Sprint 4 – Enterprise ATS Analysis Engine

### Current Sprint

🚧 **Sprint 5 – AI Resume Optimizer**

### Repository Highlights

- ✅ Enterprise SDLC Documentation
- ✅ Modular Python Architecture
- ✅ Centralized Logging
- ✅ SQLite Database
- ✅ File Reader (PDF, DOCX, TXT)
- ✅ Resume Parser
- ✅ Job Description Parser
- ✅ Enterprise Skill Repository
- ✅ Intelligent Skill Extractor
- ✅ Weighted ATS Analysis Engine
- ✅ ATS Report Generator

---

## 📊 Current Project Progress

```text
Sprint 1  ██████████ 100%
Sprint 2  ██████████ 100%
Sprint 3  ██████████ 100%
Sprint 4  ██████████ 100%
Sprint 5  ░░░░░░░░░░   0%
Sprint 6  ░░░░░░░░░░   0%
Sprint 7  ░░░░░░░░░░   0%
Sprint 8  ░░░░░░░░░░   0%

Overall Progress ≈ 50%
```

---

## ⭐ If you found this project interesting, please consider giving it a Star!

Your support helps motivate further development and improvements.