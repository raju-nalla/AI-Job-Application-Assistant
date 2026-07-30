"""
database.py

Database management module for
AI Job Application Assistant.

Responsibilities:
- Create SQLite database
- Create application tables
- Provide database connection
- Initialize database

Author: Raju Nalla
"""

import sqlite3
from pathlib import Path

from modules.logger import get_logger

logger = get_logger(__name__)

# -------------------------------------------------------------------
# Database Configuration
# -------------------------------------------------------------------

DATABASE_DIR = Path("data/database")
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "job_tracker.db"


# -------------------------------------------------------------------
# Database Connection
# -------------------------------------------------------------------

def get_connection() -> sqlite3.Connection:
    """
    Returns a SQLite database connection.

    Returns:
        sqlite3.Connection
    """

    try:
        connection = sqlite3.connect(DATABASE_FILE)
        connection.row_factory = sqlite3.Row

        logger.info("Database connection established.")

        return connection

    except sqlite3.Error as error:
        logger.error(f"Database connection failed: {error}")
        raise


# -------------------------------------------------------------------
# Database Initialization
# -------------------------------------------------------------------

def initialize_database() -> None:
    """
    Creates all required database tables.
    """

    logger.info("Initializing database...")

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # ---------------------------------------------------------
        # Users
        # ---------------------------------------------------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            user_id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            email TEXT UNIQUE,

            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
        """)

        # ---------------------------------------------------------
        # Resumes
        # ---------------------------------------------------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (

            resume_id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            file_name TEXT,

            uploaded_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            extracted_skills TEXT,

            experience TEXT,

            education TEXT,

            FOREIGN KEY(user_id)
                REFERENCES users(user_id)

        );
        """)

        # ---------------------------------------------------------
        # Job Descriptions
        # ---------------------------------------------------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_descriptions (

            jd_id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            job_title TEXT,

            skills TEXT,

            experience TEXT,

            responsibilities TEXT,

            uploaded_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
        """)

        # ---------------------------------------------------------
        # ATS Results
        # ---------------------------------------------------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ats_results (

            ats_id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_id INTEGER,

            jd_id INTEGER,

            ats_score REAL,

            missing_skills TEXT,

            recommendations TEXT,

            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(resume_id)
                REFERENCES resumes(resume_id),

            FOREIGN KEY(jd_id)
                REFERENCES job_descriptions(jd_id)

        );
        """)

        # ---------------------------------------------------------
        # Cover Letters
        # ---------------------------------------------------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cover_letters (

            cover_letter_id INTEGER PRIMARY KEY AUTOINCREMENT,

            ats_id INTEGER,

            company TEXT,

            generated_file TEXT,

            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(ats_id)
                REFERENCES ats_results(ats_id)

        );
        """)

        # ---------------------------------------------------------
        # Applications
        # ---------------------------------------------------------

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (

            application_id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT NOT NULL,

            position TEXT NOT NULL,

            application_date DATE,

            status TEXT,

            recruiter TEXT,

            notes TEXT

        );
        """)

        connection.commit()

        logger.info("Database initialized successfully.")

    except sqlite3.Error as error:
        logger.error(f"Database initialization failed: {error}")
        raise

    finally:
        if connection is not None:
            connection.close()
            logger.info("Database connection closed.")