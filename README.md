# 🚀 AI Job Application Assistant

An enterprise-grade AI-powered application that automates the job application lifecycle, including resume parsing, job description parsing, ATS analysis, resume optimization, cover letter generation, and application tracking.

The project is being developed incrementally using **Agile Scrum** and **Software Development Life Cycle (SDLC)** best practices.

---

# 📌 Project Overview

The AI Job Application Assistant helps job seekers streamline their application process by:

- 📄 Reading resumes (PDF, DOCX, TXT)
- 📄 Reading job descriptions
- 🔍 Extracting structured information
- 🎯 Comparing resumes with job descriptions
- 📝 Generating ATS-friendly resumes
- ✉️ Generating AI-powered cover letters
- 📊 Tracking job applications
- 📈 Visualizing application analytics

This project emphasizes:

- Modular Architecture
- Object-Oriented Programming
- Clean Code
- Enterprise SDLC
- Agile Development
- Production-ready Design

---

# ✅ Current Features (Sprint 3)

### Core Modules

- ✅ Centralized Logging Framework
- ✅ SQLite Database Management
- ✅ PDF, DOCX & TXT File Reader
- ✅ Resume Parser
- ✅ Job Description Parser

### Upcoming Modules

- ATS Matching Engine
- Skill Extractor
- Resume Optimizer
- Cover Letter Generator
- Application Tracker
- Analytics Dashboard

---

# 🏗 Architecture

```text
                        Streamlit UI
                             │
                             ▼
                    Business Logic Layer
                             │
       ┌─────────────────────┼─────────────────────┐
       ▼                     ▼                     ▼
 Resume Parser      JD Parser          ATS Engine
       │                     │
       └──────────────┬──────┘
                      ▼
                SQLite Database
                      │
                      ▼
              Reports / Generated Files
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
│   ├── resumes/
│   └── job_descriptions/
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
│   └── job_description_parser.py
│
├── prompts/
├── reports/
├── templates/
├── tests/
└── tracker/
```

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

## Run Application

```bash
streamlit run app.py
```

---

# 📅 Development Roadmap

| Sprint | Deliverable | Status |
|---------|-------------|--------|
| Sprint 1 | Project Setup | ✅ Completed |
| Sprint 2 | Architecture & Design | ✅ Completed |
| Sprint 3 | Core Parsing Modules | ✅ Completed |
| Sprint 4 | ATS Matching Engine | 🚧 In Progress |
| Sprint 5 | AI Resume Optimizer | ⏳ Planned |
| Sprint 6 | AI Cover Letter Generator | ⏳ Planned |
| Sprint 7 | Streamlit Dashboard | ⏳ Planned |
| Sprint 8 | Deployment | ⏳ Planned |

---

# 🎯 Future Enhancements

- FastAPI REST APIs
- PostgreSQL Support
- Azure Cloud Deployment
- User Authentication
- Multi-user Support
- AI Career Coach
- Interview Preparation Assistant
- Recruiter CRM
- Job Recommendation Engine
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
- ✅ Sprint 2 – Software Design
- ✅ Sprint 3 – Core Parsing Modules

### Current Sprint

🚧 **Sprint 4 – ATS Matching Engine**

### Repository Progress

- ✅ Enterprise Project Structure
- ✅ SDLC Documentation
- ✅ Modular Python Architecture
- ✅ Centralized Logging
- ✅ SQLite Database
- ✅ File Reader
- ✅ Resume Parser
- ✅ Job Description Parser

---

## ⭐ If you found this project interesting, please consider giving it a Star!