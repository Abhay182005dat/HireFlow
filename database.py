import sqlite3

def setup_database():
    conn  = sqlite3.connect("HireFlow.db")
    cursor = sqlite3.connect("HireFlow.db").cursor()

    # Job descriptions Table
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            description TEXT,
            summary TEXT        
        )
    """)
    # Storing Resumes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            skills TEXT,
            experience TEXT,
            education TEXT
        )
    """)

    # storing match scores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS match_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_id INTEGER,
            job_id INTEGER,
            score REAL,
            shortlisted INTEGER DEFAULT 0,
            FOREIGN KEY(resume_id) REFERENCES resumes(id),
            FOREIGN KEY(job_id) REFERENCES jobs(id)
        )
    """)

    # Storing scheduled interviews
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_id INTEGER,
            job_id INTEGER,
            interview_date TEXT,
            email_sent INTEGER DEFAULT 0,
            FOREIGN KEY(resume_id) REFERENCES resumes(id),
            FOREIGN KEY(job_id) REFERENCES jobs(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database Setup Complete")

if __name__ == "__main__" :
    setup_database()


