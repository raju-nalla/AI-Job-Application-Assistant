# 🚀 AI Job Application Assistant

An AI-powered application that automates the complete job application lifecycle, including job description parsing, ATS compatibility analysis, resume optimization, cover letter generation, and application tracking.

---

## 📌 Project Overview

AI Job Application Assistant is an enterprise-style software project developed using Software Development Life Cycle (SDLC) principles.

The application helps job seekers:

- 📄 Parse Job Descriptions
- 📄 Parse Resumes
- 🎯 Calculate ATS Match Score
- 📝 Generate ATS-Optimized Resumes
- ✉️ Generate Cover Letters
- 📊 Track Job Applications
- 📈 Visualize Application Analytics

The project is being developed incrementally using Agile sprints and emphasizes clean architecture, modular design, and maintainable code.

---

# ✨ Features

## Current (MVP)

- Resume Parser
- Job Description Parser
- ATS Match Engine
- Resume Generator
- Cover Letter Generator
- Application Tracker
- Analytics Dashboard

---

# 🏗 Architecture

```
                    Streamlit UI
                         │
                         ▼
                Business Logic Layer
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Resume Parser     JD Parser       ATS Engine
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  SQLite Database
                         │
                         ▼
                  Reports / Files
```

---

# 📁 Project Structure

```
AI-Job-Application-Assistant/

│
├── app.py
├── requirements.txt
├── README.md
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
│
├── modules/
│
├── prompts/
│
├── reports/
│
├── templates/
│
├── tests/
│
└── tracker/
```

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| UI | Streamlit |
| Database | SQLite |
| AI | OpenAI API |
| Data Processing | Pandas |
| Document Processing | pdfplumber, python-docx |
| Visualization | Plotly |
| Version Control | Git & GitHub |

---

# 📂 Documentation

The project includes comprehensive design documentation.

| Document | Description |
|----------|-------------|
| Project Charter | Project objectives and vision |
| Software Requirements Specification | Functional and non-functional requirements |
| High-Level Design | Overall architecture |
| Low-Level Design | Module-level implementation details |
| Database Design | Database schema and relationships |
| UI Wireframes | User interface design |
| Sprint Backlog | Agile sprint planning |
| Project Roadmap | Development roadmap |

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

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

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
| Sprint 3 | Resume & JD Parser | 🚧 In Progress |
| Sprint 4 | ATS Engine | ⏳ Planned |
| Sprint 5 | Resume Generator | ⏳ Planned |
| Sprint 6 | Cover Letter Generator | ⏳ Planned |
| Sprint 7 | Dashboard | ⏳ Planned |
| Sprint 8 | Deployment | ⏳ Planned |

---

# 🎯 Future Enhancements

- REST APIs (FastAPI)
- PostgreSQL Support
- Azure Deployment
- User Authentication
- Multi-user Support
- AI Career Coach
- Interview Preparation
- Recruiter CRM
- Job Recommendation Engine

---

# 🤝 Contributing

Contributions, ideas, and feedback are welcome.

Please fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Raju Nalla**

- Azure Data Engineer
- Python Developer
- Data Engineering Enthusiast

GitHub:
https://github.com/raju-nalla

LinkedIn:
https://www.linkedin.com/in/raju-nalla

---

# ⭐ Project Status

🚧 Active Development

Current Sprint: **Sprint 3 – Resume & Job Description Parser**