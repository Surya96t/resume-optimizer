import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv(override=True)

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_resume(md_resume, job_description):
    """Process resume with OpenAI and return structured results."""
    SYSTEM_PROMPT = """You are a professional resume optimization expert. 
    Analyze job descriptions and resumes to provide targeted improvements 
    while maintaining authenticity."""
    
    # Original Prompt
    USER_PROMPT = f"""
    I need to optimize my resume for this job description. Please provide:
    1. A list of keywords from the job description to include (comma-separated)
    2. An improved markdown resume with these keywords integrated naturally
    
    Format your response EXACTLY like this:
    ###KEYWORDS###
    keyword1, keyword2, keyword3
    ###RESUME###
    [full markdown resume here]

    Job Description:
    {job_description}

    Current Resume (Markdown):
    {md_resume}
    """
    # Prompt to test
    # USER_PROMPT = f"""
    # I have a resume formatted in Markdown and a job description. \
    # Please adapt my resume to better align with the job requirements while \
    # maintaining a professional tone. Tailor my skills, experiences, and \
    # achievements to highlight the most relevant points for the position. \
    # Ensure that my resume still reflects my unique qualifications and strengths \
    # but emphasizes the skills and experiences that match the job description.

    # ### Here is my resume in Markdown:
    # {md_resume}

    # ### Here is the job description:
    # {job_description}

    # Please modify the resume to:
    # - Use keywords and phrases from the job description.
    # - Adjust the bullet points under each role to emphasize relevant skills and achievements.
    # - Make sure my experiences are presented in a way that matches the required qualifications.
    # - Maintain clarity, conciseness, and professionalism throughout.

    # Return the updated resume in Markdown format.
    # """
    
    
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Update to current model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT}
            ],
            temperature=0.25,
            max_tokens=2000
        )
        
        content = response.choices[0].message.content
        
        # Parse the response
        keywords_section, resume_section = content.split("###RESUME###")
        keywords = keywords_section.replace("###KEYWORDS###", "").strip().split(", ")
        
        return {
            "keywords": keywords,
            "optimized_resume": resume_section.strip()
        }
        
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/optimize', methods=['POST'])
def handle_optimization():
    data = request.json
    result = optimize_resume(
        md_resume=data.get('resume'),
        job_description=data.get('job_description')
    )
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)