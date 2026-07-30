# High Level Design (HLD)

# AI Job Application Assistant

**Version:** 1.0  
**Author:** Raju Nalla  
**Sprint:** 2  
**Document Type:** High Level Design (HLD)

---

# 1. Introduction

## 1.1 Purpose

This High-Level Design (HLD) document describes the overall architecture, system components, module interactions, technology stack, and data flow for the AI Job Application Assistant. It serves as a blueprint for development and ensures that the application is scalable, maintainable, and modular.

---

# 2. System Overview

The AI Job Application Assistant is an AI-powered application that helps job seekers automate and streamline their job application process.

The system provides the following capabilities:

- Parse Job Descriptions
- Parse Resumes
- Calculate ATS Match Score
- Generate ATS Optimized Resume
- Generate Cover Letters
- Track Job Applications
- Display Analytics Dashboard

---

# 3. System Architecture

```
                        +-------------------------+
                        |     Streamlit UI        |
                        +-----------+-------------+
                                    |
                                    v
                    +---------------+---------------+
                    |      Business Logic Layer     |
                    +---------------+---------------+
                                    |
        +-------------+-------------+-------------+-------------+
        |             |             |             |             |
        v             v             v             v             v
 JD Parser      Resume Parser   ATS Engine   AI Generator   Tracker
        |             |             |             |             |
        +-------------+-------------+-------------+-------------+
                                    |
                                    v
                         SQLite Database
                                    |
                                    v
                              Reports / Files
```

---

# 4. Architecture Layers

## 4.1 Presentation Layer

Responsible for user interaction.

Technology:

- Streamlit

Responsibilities:

- Upload Resume
- Upload Job Description
- Display ATS Score
- Generate Resume
- Generate Cover Letter
- Dashboard

---

## 4.2 Business Logic Layer

Responsible for processing user requests and coordinating between modules.

Responsibilities:

- Validate Inputs
- Call Parser Modules
- ATS Calculation
- AI Prompt Processing
- Application Tracking

---

## 4.3 Data Layer

Responsible for data storage.

Technology:

- SQLite

Stores

- User Information
- Job Details
- Resume Metadata
- ATS Results
- Application Status

---

# 5. Functional Modules

## Module 1 – Dashboard

Responsibilities

- Overview Metrics
- ATS Statistics
- Application Status
- Charts

---

## Module 2 – Job Description Parser

Responsibilities

- Read PDF
- Read DOCX
- Read Text
- Extract Keywords
- Extract Skills
- Extract Experience
- Extract Responsibilities

Input

- PDF
- DOCX
- Text

Output

Structured Job Description

---

## Module 3 – Resume Parser

Responsibilities

- Read Resume
- Extract Skills
- Extract Experience
- Extract Education
- Extract Certifications
- Extract Projects

Output

Structured Resume Data

---

## Module 4 – ATS Match Engine

Responsibilities

- Compare Resume
- Compare Job Description
- Calculate ATS Score
- Identify Missing Skills
- Generate Suggestions

Output

- Match Percentage
- Missing Keywords
- Recommendations

---

## Module 5 – Resume Generator

Responsibilities

- Optimize Resume
- Reorder Skills
- Improve Keywords
- Export DOCX
- Export PDF

---

## Module 6 – Cover Letter Generator

Responsibilities

- Generate Cover Letter
- Recruiter Email
- LinkedIn Message

---

## Module 7 – Application Tracker

Responsibilities

- Save Applications
- Track Status
- Update Interview Progress
- Store Notes

---

## Module 8 – Analytics Dashboard

Responsibilities

- ATS Trend
- Skills Gap
- Application Summary
- Interview Success Rate

---

# 6. Data Flow

```
User

↓

Upload Resume

↓

Resume Parser

↓

Structured Resume

↓

Upload Job Description

↓

JD Parser

↓

Structured Job Description

↓

ATS Match Engine

↓

AI Resume Generator

↓

Cover Letter Generator

↓

Application Tracker

↓

Dashboard
```

---

# 7. Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI | OpenAI API |
| Database | SQLite |
| Data Processing | Pandas |
| File Processing | pdfplumber, python-docx |
| Visualization | Plotly |
| Version Control | Git & GitHub |

---

# 8. Security Considerations

- Secure API key management using environment variables
- Input validation for uploaded files
- Local database storage
- Error handling and logging
- File size validation

---

# 9. Logging Strategy

The application maintains logs for:

- Application Startup
- User Activity
- AI Requests
- Errors
- ATS Calculations
- Resume Generation

Log files will be stored in the `logs/` directory.

---

# 10. Error Handling

The system shall handle:

- Invalid PDF/DOCX files
- Missing Resume
- Missing Job Description
- AI API failures
- Database errors
- File upload errors

---

# 11. Scalability

The architecture is designed to support future enhancements such as:

- LinkedIn Integration
- Gmail Integration
- Multiple Resume Templates
- Multi-User Support
- Cloud Database
- Azure Deployment
- AI Career Coach
- Interview Simulator

---

# 12. Assumptions

- Users have internet connectivity.
- OpenAI API is available.
- Supported document formats are PDF, DOCX, and TXT.
- Users upload valid resume and job description files.

---

# 13. High-Level Workflow

```
User
   │
   ▼
Streamlit UI
   │
   ▼
Business Logic
   │
   ├────────► Resume Parser
   │
   ├────────► JD Parser
   │
   ├────────► ATS Engine
   │
   ├────────► Resume Generator
   │
   ├────────► Cover Letter Generator
   │
   └────────► Application Tracker
              │
              ▼
         SQLite Database
              │
              ▼
      Dashboard & Reports
```

---

# 14. Future Enhancements

- AI Interview Coach
- AI Career Advisor
- Job Recommendation Engine
- Recruiter Contact Generator
- Email Automation
- Calendar Integration
- Resume Version Management
- Multi-language Support

---

# 15. Conclusion

The proposed architecture follows a layered and modular design, making the application easy to maintain, extend, and scale. Each module has a clearly defined responsibility, enabling independent development and testing while supporting future enhancements without major architectural changes.