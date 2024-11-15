from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from docx import Document
import PyPDF2
import re

def ext_s_role(text):
    skills = ['Python', 'Django', 'JavaScript', 'HTML', 'CSS', 'SQL', 'Git','numpy','pandas','plotlib','seaborn']
    roles = ['Developer', 'Engineer', 'Analyst','Data Analysis','Data Science']

    extracted_skills = [skill for skill in skills if skill.lower() in text.lower()]
    extracted_roles = [role for role in roles if role.lower() in text.lower()]

    return extracted_skills, extracted_roles

def read_resume(file):
    if file.name.endswith('.docx'):
        doc = Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file.name.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        return '\n'.join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    else:
        return file.read().decode('utf-8')  

def cal_m_p(resume_text, job_desc_text):
    resume_skills, resume_roles = ext_s_role(resume_text)
    job_skills, job_roles = ext_s_role(job_desc_text)

    total_points = 0
    score = 0

    # Assign points for skills
    for skill in resume_skills:
        if skill in job_skills:
            score += 10 
        total_points += 10  

    # Assign points for roles
    for role in resume_roles:
        if role in job_roles:
            score += 10  
        total_points += 10  

    # Calculate percentage
    match_percentage = (score / total_points) * 100 if total_points > 0 else 0
    return match_percentage

def match_view(request):
    match_percentage = None 
    if request.method == 'POST':
        resume_file = request.FILES.get('resume')  
        job_description_file = request.FILES.get('job_description')  
        
        if resume_file and job_description_file:
            # Read the contents of the files
            resume_text = read_resume(resume_file)
            job_desc_text = read_resume(job_description_file)

            # Calculate match percentage
            match_percentage = cal_m_p(resume_text, job_desc_text)

    return render(request, 'home.html', {'match_percentage': match_percentage})