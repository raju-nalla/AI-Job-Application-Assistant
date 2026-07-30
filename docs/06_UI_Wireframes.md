# UI Wireframes

# AI Job Application Assistant

**Version:** 1.0  
**Author:** Raju Nalla  
**Sprint:** 2  
**Document Type:** UI Wireframes

---

# 1. Introduction

This document describes the user interface layout for the AI Job Application Assistant.

The application follows a simple dashboard-driven interface where users can upload documents, perform ATS analysis, generate resumes and cover letters, track applications, and view analytics.

---

# 2. Application Navigation

```
-----------------------------------------------------
           AI Job Application Assistant
-----------------------------------------------------

🏠 Dashboard

📄 Resume Parser

📋 Job Description Parser

🎯 ATS Match

📝 Resume Generator

✉️ Cover Letter Generator

📊 Application Tracker

📈 Analytics

⚙️ Settings
```

---

# 3. Dashboard Screen

```
--------------------------------------------------------------
               AI Job Application Assistant
--------------------------------------------------------------

Total Applications      Interviews      Offers      ATS Avg

      35                    8              2          84%

--------------------------------------------------------------

Recent Applications

--------------------------------------------------------------
Company          Position          Status
--------------------------------------------------------------
Microsoft        Data Engineer     Interview
Amazon           Data Engineer     Applied
EY               Azure Engineer    Rejected
--------------------------------------------------------------

[ Upload Resume ]

[ Upload Job Description ]

[ Start ATS Analysis ]
```

---

# 4. Resume Parser Screen

```
---------------------------------------------------------

Resume Parser

---------------------------------------------------------

Upload Resume

[ Choose File ]

Supported Formats

✔ PDF

✔ DOCX

---------------------------------------------------------

Extracted Information

---------------------------------------------------------

Name

Skills

Experience

Education

Projects

Certifications

---------------------------------------------------------

[ Parse Resume ]
```

---

# 5. Job Description Parser Screen

```
---------------------------------------------------------

Job Description Parser

---------------------------------------------------------

Upload Job Description

[ Choose File ]

Supported Formats

✔ PDF

✔ DOCX

✔ TXT

---------------------------------------------------------

Extracted Details

---------------------------------------------------------

Company

Job Title

Required Skills

Experience

Education

Responsibilities

---------------------------------------------------------

[ Parse Job Description ]
```

---

# 6. ATS Match Screen

```
---------------------------------------------------------

ATS Match Analysis

---------------------------------------------------------

Resume

✔ Uploaded

Job Description

✔ Uploaded

---------------------------------------------------------

ATS Score

87%

---------------------------------------------------------

Matched Skills

✔ SQL

✔ Python

✔ Azure

✔ Databricks

---------------------------------------------------------

Missing Skills

• Kafka

• Terraform

• Docker

---------------------------------------------------------

Recommendations

✔ Add Kafka Experience

✔ Highlight Databricks Projects

✔ Include Azure DevOps

---------------------------------------------------------

[ Generate ATS Resume ]
```

---

# 7. Resume Generator Screen

```
---------------------------------------------------------

Resume Generator

---------------------------------------------------------

ATS Score

87%

---------------------------------------------------------

Template

( ) Professional

( ) Modern

( ) Executive

---------------------------------------------------------

Output Format

✔ DOCX

✔ PDF

---------------------------------------------------------

[ Generate Resume ]

---------------------------------------------------------

Download

Resume.docx

Resume.pdf
```

---

# 8. Cover Letter Generator

```
---------------------------------------------------------

Cover Letter Generator

---------------------------------------------------------

Company

Microsoft

Position

Senior Data Engineer

Hiring Manager

(Optional)

---------------------------------------------------------

Tone

Professional

Friendly

Formal

---------------------------------------------------------

[ Generate Cover Letter ]

---------------------------------------------------------

Download

CoverLetter.docx

CoverLetter.pdf
```

---

# 9. Application Tracker

```
---------------------------------------------------------

Application Tracker

---------------------------------------------------------

Company

Position

Status

Applied Date

Recruiter

Notes

---------------------------------------------------------

Microsoft

Azure Data Engineer

Interview

30-Jul-2026

John Smith

Round-2 Scheduled

---------------------------------------------------------

[ Add Application ]

[ Update Status ]

[ Delete ]
```

---

# 10. Analytics Dashboard

```
---------------------------------------------------------

Analytics Dashboard

---------------------------------------------------------

Applications by Status

Applied

Interview

Rejected

Offer

---------------------------------------------------------

ATS Score Trend

(Line Chart)

---------------------------------------------------------

Top Skills

SQL

Python

Azure

Databricks

Snowflake

---------------------------------------------------------

Applications per Month

(Bar Chart)
```

---

# 11. Settings Screen

```
---------------------------------------------------------

Settings

---------------------------------------------------------

OpenAI API Key

************************

Theme

Light

Dark

Database

SQLite

Output Folder

data/generated/

---------------------------------------------------------

[ Save Settings ]
```

---

# 12. User Workflow

```
Login

↓

Dashboard

↓

Upload Resume

↓

Resume Parsing

↓

Upload Job Description

↓

Job Description Parsing

↓

ATS Analysis

↓

Resume Generation

↓

Cover Letter Generation

↓

Application Tracking

↓

Analytics Dashboard
```

---

# 13. Design Principles

The application follows these UI design principles:

- Clean and minimal interface
- Dashboard-first navigation
- Responsive layout
- Simple file upload process
- One-click document generation
- Clear progress indicators
- Easy download options
- User-friendly error messages

---

# 14. Future UI Enhancements

Future versions of the application may include:

- Multi-page navigation
- Dark mode
- User authentication
- Drag-and-drop file uploads
- Interactive charts
- AI chatbot assistant
- Mobile-responsive layout
- Multi-user support

---

# 15. Conclusion

The proposed wireframes provide a simple and intuitive user interface that supports the complete job application workflow. The layout is designed to minimize user effort while providing quick access to core features such as ATS analysis, resume generation, cover letter generation, application tracking, and analytics.