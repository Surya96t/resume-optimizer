def create_prompt(resume_string: str, jd_string: str) -> str:
    """
    Creates a detailed prompt for AI-powered resume optimization based on a job description.

    This function generates a structured prompt that guides the AI to:
    - Tailor the resume to match job requirements
    - Optimize for ATS systems
    - Provide actionable improvement suggestions
    - Format the output in clean Markdown

    Args:
        resume_string (str): The input resume text
        jd_string (str): The target job description text

    Returns:
        str: A formatted prompt string containing instructions for resume optimization
    """
    return f"""
    You are a professional resume optimization expert specializing in tailoring resumes to specific job descriptions. Your goal is to optimize my resume and provide actionable suggestions for improvement to align with the target role.

    ### Guidelines:
    1. **Relevance**:  
        - Prioritize experiences, skills, and achievements **most relevant to the job description**.  
        - Remove or de-emphasize irrelevant details to ensure a **concise** and **targeted** resume.
        - Limit work experience section to 2-3 most relevant roles
        - Limit bullet points under each role to 2-3 most relevant impacts

    2. **Action-Driven Results**:  
        - Use **strong action verbs** and **quantifiable results** (e.g., percentages, revenue, efficiency improvements) to highlight impact.  

    3. **Keyword Optimization**:  
        - Integrate **keywords** and phrases from the job description naturally to optimize for ATS (Applicant Tracking Systems).  

    4. **Additional Suggestions** *(If Gaps Exist)*:  
    - If the resume does not fully align with the job description, suggest:  
        1. **Additional technical or soft skills** that I could add to make my profile stronger.  
        2. **Certifications or courses** I could pursue to bridge the gap.  
        3. **Project ideas or experiences** that would better align with the role.  

    5. **Formatting**:  
        - Output the tailored resume in **clean Markdown format**.  
        - Include an **"Additional Suggestions"** section at the end with actionable improvement recommendations.  

    ---

    ### Input:
    - **My resume**:  
    {resume_string}

    - **The job description**:  
    {jd_string}

    ---

    ### Output:  
    1. **Tailored Resume**:  
        - A resume in **Markdown format** that emphasizes relevant experience, skills, and achievements.  
        - Incorporates job description **keywords** to optimize for ATS.  
        - Uses strong language and is no longer than **one page**.

    2. **Additional Suggestions** *(if applicable)*:  
        - List **skills** that could strengthen alignment with the role.  
        - Recommend **certifications or courses** to pursue.  
        - Suggest **specific projects or experiences** to develop.
    """