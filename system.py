from PIL import Image
import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from a PDF file


def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file.

    Args:
        file (PdfReader): The PDF file to extract text from.

    Returns:
        str: The extracted text.
    """
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Function to rank resumes based on their job description


def rank_resumes(job_description, resumes):
    """
    Ranks resumes based on their similarity to the job description.

    Args:
        job_description (str): The job description.
        resumes (list): A list of resume texts.

    Returns:
        list: A list of cosine similarities between the job description and each resume.
    """
    # Combine job description with resumes
    documents = [job_description] + resumes

    # Create a TfidfVectorizer and fit it to the documents
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents).toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity(
        [job_description_vector], resume_vectors).flatten()

    return cosine_similarities

# Function to generate key points based on resume content


def generate_key_points(resume_text):
    """
    Generates key points based on the content of the resume.

    Args:
        resume_text (str): The text of the resume.

    Returns:
        list: A list of key points for resume improvement.
    """

    # to generate key points based on keywords found in the resume
    key_points = set()
    if "web developer" in resume_text.lower():
        key_points.add(
            "Add Some Web Development Course Certificates to your Resume.")

    if "software engineer" in resume_text.lower():
        key_points.add(
            "Highlight your coding projects and include links to GitHub repositories.")

    if "data scientist" in resume_text.lower():
        key_points.add(
            "Include Data Science Certifications and Kaggle competition experience.")

    if "database administrator" in resume_text.lower():
        key_points.add(
            "Showcase SQL expertise and any database management certifications.")

    if "systems administrator" in resume_text.lower():
        key_points.add(
            "Highlight experience with system configurations, backups, and troubleshooting.")

    if "network engineer" in resume_text.lower():
        key_points.add(
            "List networking certifications like CCNA, CCNP to boost your profile.")

    if "ux/ui designer" in resume_text.lower():
        key_points.add(
            "Add a portfolio link showcasing UI/UX design projects.")

    if "it security analyst" in resume_text.lower():
        key_points.add(
            "Include cybersecurity certifications like CEH, CISSP, or CompTIA Security+.")

    if "cloud engineer" in resume_text.lower():
        key_points.add(
            "Mention cloud platform expertise (AWS, Azure, GCP) and relevant certifications.")

    if "machine learning engineer" in resume_text.lower():
        key_points.add(
            "Showcase machine learning projects and model deployments.")

    if "devops engineer" in resume_text.lower():
        key_points.add(
            "Highlight experience with CI/CD, Docker, Kubernetes, and automation tools.")

    if "business analyst" in resume_text.lower():
        key_points.add(
            "Include experience with data visualization tools like Power BI or Tableau.")

    if "full stack developer" in resume_text.lower():
        key_points.add(
            "Mention proficiency in both frontend and backend technologies.")

    if "cybersecurity specialist" in resume_text.lower():
        key_points.add(
            "List certifications and experience in ethical hacking, threat analysis, and risk management.")

    if "ai engineer" in resume_text.lower():
        key_points.add(
            "Mention deep learning, NLP experience, and AI framework expertise.")

    if "game developer" in resume_text.lower():
        key_points.add(
            "Showcase projects using Unity, Unreal Engine, or game development tools.")

    if "technical support specialist" in resume_text.lower():
        key_points.add(
            "Highlight problem-solving skills and IT support experience.")

    if "blockchain developer" in resume_text.lower():
        key_points.add(
            "Showcase blockchain project experience and knowledge of smart contracts.")

    if "embedded systems engineer" in resume_text.lower():
        key_points.add(
            "Mention experience with microcontrollers, IoT devices, and real-time systems.")

    if "robotics engineer" in resume_text.lower():
        key_points.add(
            "Highlight robotics programming skills and hands-on experience.")

    if "quantitative analyst" in resume_text.lower():
        key_points.add(
            "Showcase experience in quantitative finance, modeling, and risk analysis.")

    if "android developer" in resume_text.lower():
        key_points.add("Add Some Android Course Certificates to your Resume.")

    if "leadership" in resume_text.lower():
        key_points.add("Highlight your leadership experiences.")

    if "project management" in resume_text.lower():
        key_points.add("Include specific projects you've managed.")

    if "certification" in resume_text.lower():
        key_points.add("List relevant certifications.")

    if "skills" in resume_text.lower():
        key_points.add("Emphasize your technical skills.")

    if "teamwork" in resume_text.lower():
        key_points.add("Showcase your teamwork abilities.")

    if "problem-solving" in resume_text.lower():
        key_points.add("Detail your problem-solving skills.")

    if "awards" in resume_text.lower():
        key_points.add("Mention any awards or recognitions received.")

    if "volunteer" in resume_text.lower():
        key_points.add("Include volunteer experiences.")

    if "communication" in resume_text.lower():
        key_points.add("Highlight your communication skills.")

    if "adaptability" in resume_text.lower():
        key_points.add("Discuss your adaptability in changing environments.")

    if "software" in resume_text.lower():
        key_points.add("Mention your proficiency in specific software.")

    if "metrics" in resume_text.lower():
        key_points.add("Include metrics to quantify your achievements.")

    if "pressure" in resume_text.lower():
        key_points.add("Highlight your ability to work under pressure.")

    if "cross-functional" in resume_text.lower():
        key_points.add("Discuss your experience with cross-functional teams.")

    if "strategic planning" in resume_text.lower():
        key_points.add("Mention your strategic planning skills.")

    if "budgeting" in resume_text.lower():
        key_points.add(
            "Include any experience with budgeting or financial management.")

    if "customer service" in resume_text.lower():
        key_points.add("Highlight your customer service skills.")

    if "data analysis" in resume_text.lower():
        key_points.add("Discuss your experience with data analysis.")

    if "mentoring" in resume_text.lower():
        key_points.add("Mention your ability to mentor or train others.")

    if "conflict resolution" in resume_text.lower():
        key_points.add("Include your experience with conflict resolution.")

    if "creativity" in resume_text.lower():
        key_points.add("Highlight your creativity and innovation.")

    if "technical writing" in resume_text.lower():
        key_points.add("Highlight your skills in technical writing.")

    return list(key_points)


# This code displays the Website Logo.
logo_path = r"C:\Users\malli\OneDrive\Desktop\Py_Codes\Ai_Resume_Analyser\logo_image\smart-resume-analyser-logo.png"
logo = Image.open(logo_path)

# Using columns to align the logo to the left
col1, col2 = st.columns([1, 3])
with col1:
    st.image(logo, width=260)  # The width can be adjustable
with col2:
    st.title("Smart Resume Analyser")
    st.write("Build ATS-friendly Resumes in seconds..")

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter your job description properly.")

# File uploader
st.header("Upload your Resume")
uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

if uploaded_file and job_description:
    st.header("Resume Analysis")

    # Extract text from uploaded resume
    resume_text = extract_text_from_pdf(uploaded_file)

    # Rank resume
    scores = rank_resumes(job_description, [resume_text])

    # Display score
    st.write("Resume Score: ", scores[0])

    # Generate and display key points for resume
    st.header("Suggested Key Points for your Resume")
    key_points = generate_key_points(resume_text)
    for point in key_points:
        st.write(f"- {point}")

    # YouTube Video Recommendations
    st.header("YouTube Video Recommendations")
    # video recommendations based on key points
    video_recommendations = {
        # Web Development
        "Add Some Web Development Course Certificates to your Resume.": "https://www.youtube.com/watch?v=DPnqb74Smug",

        # Software Engineering
        "Highlight your coding projects and include links to GitHub repositories.": "https://www.youtube.com/watch?v=wpISo9TNjfU",

        # Data Science
        "Include Data Science Certifications and Kaggle competition experience.": "https://www.youtube.com/watch?v=ua-CiDNNj30",

        # Database Administration
        "Showcase SQL expertise and any database management certifications.": "https://www.youtube.com/watch?v=7S_tz1z_5bA",

        # Systems Administration
        "Highlight experience with system configurations, backups, and troubleshooting.": "https://www.youtube.com/watch?v=Y8hXt9Pyv4M",

        # Network Engineering
        "List networking certifications like CCNA, CCNP to boost your profile.": "https://www.youtube.com/watch?v=qiQR5rTSshw",

        # UI/UX Design
        "Add a portfolio link showcasing UI/UX design projects.": "https://www.youtube.com/watch?v=GJjMjSDZhtU",

        # IT Security Analyst
        "Include cybersecurity certifications like CEH, CISSP, or CompTIA Security+.": "https://www.youtube.com/watch?v=vv6tqxLjjRI",

        # Cloud Engineering
        "Mention cloud platform expertise (AWS, Azure, GCP) and relevant certifications.": "https://www.youtube.com/watch?v=ulprqHHWlng",

        # Machine Learning Engineer
        "Showcase machine learning projects and model deployments.": "https://www.youtube.com/watch?v=Gv9_4yMHFhI",

        # DevOps Engineer
        "Highlight experience with CI/CD, Docker, Kubernetes, and automation tools.": "https://www.youtube.com/watch?v=WMy1nFofmZ8",

        # Business Analyst
        "Include experience with data visualization tools like Power BI or Tableau.": "https://www.youtube.com/watch?v=AGrl-H87pRU",

        # Full Stack Developer
        "Mention proficiency in both frontend and backend technologies.": "https://www.youtube.com/watch?v=nu_pCVPKzTk",

        # Cybersecurity Specialist
        "List certifications and experience in ethical hacking, threat analysis, and risk management.": "https://www.youtube.com/watch?v=3Kq1MIfTWCE",

        # AI Engineer
        "Mention deep learning, NLP experience, and AI framework expertise.": "https://www.youtube.com/watch?v=aircAruvnKk",

        # Game Developer
        "Showcase projects using Unity, Unreal Engine, or game development tools.": "https://www.youtube.com/watch?v=IxiWurU0-tE",

        # Technical Support Specialist
        "Highlight problem-solving skills and IT support experience.": "https://www.youtube.com/watch?v=Fi1w8rJjMq8",

        # Blockchain Developer
        "Showcase blockchain project experience and knowledge of smart contracts.": "https://www.youtube.com/watch?v=HXoVSbwWUIk",

        # Embedded Systems Engineer
        "Mention experience with microcontrollers, IoT devices, and real-time systems.": "https://www.youtube.com/watch?v=l1M3Krt-fQY",

        # Robotics Engineer
        "Highlight robotics programming skills and hands-on experience.": "https://www.youtube.com/watch?v=xS3s7I6g1Zw",

        # Quantitative Analyst
        "Showcase experience in quantitative finance, modeling, and risk analysis.": "https://www.youtube.com/watch?v=smbvZ6wBXlA",

        # Android Developer
        "Add Some Android Course Certificates to your Resume.": "https://youtu.be/HyU4vkZ2NB8",

        # Leadership Skills
        "Highlight your leadership experiences.": "https://www.youtube.com/watch?v=JRlKKljzGI0",

        # Project Management
        "Include specific projects you've managed.": "https://www.youtube.com/watch?v=JrcjOCq7pLg",

        # Certifications
        "List relevant certifications.": "https://youtu.be/oOpdX35ZeK0?si=WwTtsqYILs9UNXTw",

        # Technical Skills
        "Emphasize your technical skills.": "https://youtu.be/Tef1e9FiSR0?si=7c9zYS_zgPRJKTuF",

        # Teamwork
        "Showcase your teamwork abilities.": "https://www.youtube.com/watch?v=wXWqYf4c97E",

        # Problem-Solving
        "Detail your problem-solving skills.": "https://youtu.be/hiqoCvPs_Jc?si=trgnc3ek8mQQVLZU",

        # Awards
        "Mention any awards or recognitions received.": "https://www.youtube.com/watch?v=sO58z-V8V5Q",

        # Volunteering
        "Include volunteer experiences.": "https://www.youtube.com/watch?v=j9uN9_4mD94",

        # Communication Skills
        "Highlight your communication skills.": "https://www.youtube.com/watch?v=icudf_w_pqU&ab_channel=ApnaCollege",

        # Adaptability
        "Discuss your adaptability in changing environments.": "https://www.youtube.com/watch?v=swbK6rppnMo",

        # Software Proficiency
        "Mention your proficiency in specific software.": "https://www.youtube.com/watch?v=I8E6uR63uXI",

        # Using Metrics
        "Include metrics to quantify your achievements.": "https://www.youtube.com/watch?v=UYJ1gk4g2kY",

        # Working Under Pressure
        "Highlight your ability to work under pressure.": "https://www.youtube.com/watch?v=WTxSmnZupxM",

        # Cross-Functional Teams
        "Discuss your experience with cross-functional teams.": "https://www.youtube.com/watch?v=z75CBV7KA60",

        # Strategic Planning
        "Mention your strategic planning skills.": "https://www.youtube.com/watch?v=gnnPNzGhO4E",

        # Budgeting
        "Include any experience with budgeting or financial management.": "https://www.youtube.com/watch?v=geHpLxMBuVk",

        # Customer Service
        "Highlight your customer service skills.": "https://www.youtube.com/watch?v=yyRW6SJW1SI",

        # Data Analysis
        "Discuss your experience with data analysis.": "https://www.youtube.com/watch?v=VPLXx0fou4M",

        # Mentoring
        "Mention your ability to mentor or train others.": "https://www.youtube.com/watch?v=1Skym90ZxWo",

        # Conflict Resolution
        "Include your experience with conflict resolution.": "https://www.youtube.com/watch?v=aDzw37zefjA",

        # Creativity
        "Highlight your creativity and innovation.": "https://www.youtube.com/watch?v=cL_8gRkKV8Q",

        # Technical Writing
        "Highlight your skills in technical writing.": "https://www.youtube.com/watch?v=ueP7IGumrl0",
    }

    for point in key_points:
        if point in video_recommendations:
            with st.expander(f"{point} - Watch This Video"):
                st.video(video_recommendations[point])

        else:
            st.write(
                f"- {point}: Sorry, No specific video recommendations found for you")
            st.write("Have a Great day.")
