# Database Design Document (DDD)

# AI Job Application Assistant

**Version:** 1.0  
**Author:** Raju Nalla  
**Sprint:** 2  
**Document Type:** Database Design

---

# 1. Introduction

## 1.1 Purpose

This document describes the database design for the AI Job Application Assistant. It defines the database architecture, tables, relationships, constraints, and storage strategy required to support the application's functionality.

---

# 2. Database Overview

The application uses **SQLite** as the primary database for Version 1.0 (MVP).

SQLite was selected because it is:

- Lightweight
- Serverless
- Easy to configure
- Suitable for local development
- Ideal for a single-user desktop application

In future versions, the database can be migrated to PostgreSQL or Azure SQL Database without significant architectural changes.

---

# 3. Database Information

| Property | Value |
|----------|-------|
| Database | SQLite |
| File Name | job_tracker.db |
| Location | data/database/ |
| Encoding | UTF-8 |

---

# 4. Database Schema

The system consists of the following tables:

1. Users
2. Resumes
3. Job_Descriptions
4. ATS_Results
5. Cover_Letters
6. Applications

---

# 5. Entity Relationship Diagram (ERD)

```
+-----------+
|   Users   |
+-----------+
      |
      | 1
      |
      | N
+-------------+
|  Resumes    |
+-------------+
      |
      | 1
      |
      | N
+--------------------+
| ATS_Results        |
+--------------------+
      |
      | N
      |
      | 1
+--------------------+
| Job_Descriptions   |
+--------------------+

Applications
     |
     |
Cover Letters
```

---

# 6. Table Design

## 6.1 Users

Purpose

Stores user profile information.

| Column | Data Type | Constraint |
|---------|-----------|------------|
| user_id | INTEGER | PRIMARY KEY |
| full_name | TEXT | NOT NULL |
| email | TEXT | UNIQUE |
| created_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |

---

## 6.2 Resumes

Purpose

Stores uploaded resumes.

| Column | Data Type | Constraint |
|---------|-----------|------------|
| resume_id | INTEGER | PRIMARY KEY |
| user_id | INTEGER | FOREIGN KEY |
| file_name | TEXT | NOT NULL |
| uploaded_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| extracted_skills | TEXT | JSON String |
| experience | TEXT | |
| education | TEXT | |

---

## 6.3 Job_Descriptions

Purpose

Stores uploaded job descriptions.

| Column | Data Type | Constraint |
|---------|-----------|------------|
| jd_id | INTEGER | PRIMARY KEY |
| company | TEXT | |
| job_title | TEXT | |
| skills | TEXT | JSON String |
| experience | TEXT | |
| responsibilities | TEXT | |
| uploaded_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |

---

## 6.4 ATS_Results

Purpose

Stores ATS comparison results.

| Column | Data Type | Constraint |
|---------|-----------|------------|
| ats_id | INTEGER | PRIMARY KEY |
| resume_id | INTEGER | FOREIGN KEY |
| jd_id | INTEGER | FOREIGN KEY |
| ats_score | REAL | |
| missing_skills | TEXT | JSON String |
| recommendations | TEXT | |
| created_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |

---

## 6.5 Cover_Letters

Purpose

Stores generated cover letters.

| Column | Data Type | Constraint |
|---------|-----------|------------|
| cover_letter_id | INTEGER | PRIMARY KEY |
| ats_id | INTEGER | FOREIGN KEY |
| company | TEXT | |
| generated_file | TEXT | |
| created_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |

---

## 6.6 Applications

Purpose

Tracks job applications.

| Column | Data Type | Constraint |
|---------|-----------|------------|
| application_id | INTEGER | PRIMARY KEY |
| company | TEXT | NOT NULL |
| position | TEXT | NOT NULL |
| application_date | DATE | |
| status | TEXT | |
| recruiter | TEXT | |
| notes | TEXT | |

---

# 7. Relationships

| Parent | Child | Relationship |
|---------|-------|--------------|
| Users | Resumes | One-to-Many |
| Resumes | ATS_Results | One-to-Many |
| Job_Descriptions | ATS_Results | One-to-Many |
| ATS_Results | Cover_Letters | One-to-One |

---

# 8. Data Flow

```
User Uploads Resume
        │
        ▼
Resume Stored
        │
        ▼
Resume Parser
        │
        ▼
Structured Resume Data
        │
        ▼
SQLite Database

----------------------------

User Uploads JD
        │
        ▼
JD Parser
        │
        ▼
Structured JD Data
        │
        ▼
SQLite Database

----------------------------

ATS Engine

↓

ATS Results Table

↓

Resume Generator

↓

Cover Letter Generator

↓

Applications Table

↓

Dashboard
```

---

# 9. Constraints

Primary Keys

- user_id
- resume_id
- jd_id
- ats_id
- cover_letter_id
- application_id

Foreign Keys

- user_id
- resume_id
- jd_id
- ats_id

Unique Constraints

- email

---

# 10. Indexing Strategy

Indexes will be created on:

- email
- company
- job_title
- ats_score
- application_date

Purpose:

- Faster searches
- Better dashboard performance
- Improved reporting

---

# 11. Backup Strategy

Version 1.0

- Manual backup of SQLite database

Future

- Scheduled backups
- Cloud storage
- Azure Blob Storage

---

# 12. Future Database Enhancements

The following tables may be added in future releases:

- Recruiters
- Companies
- Interview_Questions
- Skills
- Certifications
- Job_Alerts
- Notifications
- AI_History

---

# 13. Migration Strategy

Current Database

SQLite

Future Migration Options

- PostgreSQL
- Azure SQL Database
- MySQL

The application will use a data access layer, making database migration easier without changing business logic.

---

# 14. Security Considerations

- Local database storage
- Parameterized SQL queries
- Input validation
- File path validation
- Regular backups

---

# 15. Conclusion

The database design provides a normalized, scalable, and maintainable structure for storing application data. The schema supports the current MVP while allowing future expansion to enterprise-grade databases such as PostgreSQL or Azure SQL Database with minimal changes.