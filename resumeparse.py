import sqlite3
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

# Initialize the LLM
llm = Ollama(model="mistral")

# Prompt Template
prompt_template = PromptTemplate.from_template("""
Extract the following details from this resume:
- Full Name
- Email Address
- Phone Number
- Skills
- Education
- Work Experience

Resume:
{resume_text}

Format the output as JSON.
""")

def parse_resume(resume_text):
    prompt = prompt_template.format(resume_text=resume_text)
    parsed_data = llm.invoke(prompt)
    return parsed_data

def store_parsed_resume(resume_id, parsed_data):
    conn = sqlite3.connect("HireFlow.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO resume_parses (resume_id, parsed_json) VALUES (?, ?)""", (resume_id, parsed_data))
    conn.commit()
    conn.close()

# Test Run
if __name__ == "__main__":
    sample_resume = """
    John Doe
    Email: john.doe@example.com | Phone: 123-456-7890
    Experienced Python developer with 4 years in ML and Data Science.
    Skills: Python, TensorFlow, SQL
    Education: B.Tech in Computer Science
    Experience: Software Engineer at XYZ Inc.
    """
    output = parse_resume(sample_resume)
    print("Parsed Resume:", output)
