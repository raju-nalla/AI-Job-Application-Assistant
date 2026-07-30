# Software Requirements Specification (SRS)

# AI Job Application Assistant

Version: 1.0

Author: Raju Nalla

---

# 1. Introduction

## 1.1 Purpose

The AI Job Application Assistant is an intelligent application designed to automate and simplify the job application process. It assists users in analyzing job descriptions, optimizing resumes, generating cover letters, tracking applications, and preparing for interviews.

---

## 1.2 Scope

The system provides:

- Job Description Parsing
- ATS Match Analysis
- Resume Optimization
- Cover Letter Generation
- Interview Question Generation
- Job Application Tracking
- Dashboard & Analytics

---

# 2. Functional Requirements

## FR-1 Job Description Parser

The system shall:

- Accept Job Description as text
- Upload PDF Job Description
- Upload DOCX Job Description
- Extract required information

Output:

- Company
- Job Title
- Experience
- Skills
- Responsibilities
- Education
- Keywords

---

## FR-2 ATS Match Engine

The system shall compare

Resume

vs

Job Description

and generate

- Match Percentage
- Missing Skills
- Recommended Improvements

---

## FR-3 Resume Generator

The system shall

- Create ATS optimized resumes
- Highlight relevant skills
- Reorder experience
- Export DOCX
- Export PDF

---

## FR-4 Cover Letter Generator

Generate

- Professional Cover Letter
- Company Specific Cover Letter
- Recruiter Email

---

## FR-5 Interview Preparation

Generate

- Technical Questions
- HR Questions
- Coding Questions
- Company Specific Questions

---

## FR-6 Job Tracker

Store

- Company
- Position
- Status
- Date Applied
- Recruiter
- Notes

---

## FR-7 Dashboard

Display

- Total Applications
- Interviews
- Rejections
- Offers
- ATS Scores
- Skills Gap

---

# 3. Non-Functional Requirements

Performance

- Response < 5 seconds

Availability

- 99% Local Availability

Security

- API Keys stored securely

Maintainability

- Modular Architecture

Scalability

- Easy addition of new AI modules

---

# 4. Assumptions

- User has internet connectivity
- User provides a valid resume
- OpenAI API is available

---

# 5. Constraints

- Local SQLite Database
- Streamlit User Interface
- Python Backend