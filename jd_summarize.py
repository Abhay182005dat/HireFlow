import sqlite3
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

db_path = "HireFlow.db"

# Initialise the model
llm = Ollama(model = "mistral")

# Prompt template
prompt_template = PromptTemplate.from_template("""
Extract the following details from this Job Description:
- Job Title
- Required Skills
- Experience Level
- Key Responsibilities
- Preferred Qualifications

Job Description:
{job_description}

Format the output as JSON.
""")

def summarize_jd(job_description):
    prompt = prompt_template.format(job_description = job_description)
    summary  = llm.invoke(prompt)
    return summary

def store_summary(job_id , summary):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO job_summaries(job_id , summary) VALUES(? , ?)""" , (job_id,summary))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Example usage
    sample_jd = """
    We are looking for a Software Engineer with 3+ years of experience in Python and machine learning.
    Must have expertise in NLP, TensorFlow, and cloud deployment.
    Responsibilities include developing AI models and collaborating with data scientists.
    """
    
    jd_summary = summarize_jd(sample_jd)
    print("Summarized JD:", jd_summary)
