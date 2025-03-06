from PIL import Image
import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# This Function is to extract all the text, from the given resume.pdf by the User.
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

# This Function is to rank the resumes based on their job description


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
    key_points = []
    if "Android Developer" in resume_text.lower():
        key_points.append(
            "Add Some Android Course Certificates to your Resume.")
    if "leadership" in resume_text.lower():
        key_points.append("Highlight your leadership experiences.")
    if "project management" in resume_text.lower():
        key_points.append("Include specific projects you've managed.")
    if "certification" in resume_text.lower():
        key_points.append("List relevant certifications.")
    if "skills" in resume_text.lower():
        key_points.append("Emphasize your technical skills.")
    if "teamwork" in resume_text.lower():
        key_points.append("Showcase your teamwork abilities.")
    if "problem-solving" in resume_text.lower():
        key_points.append("Detail your problem-solving skills.")
    if "awards" in resume_text.lower():
        key_points.append("Mention any awards or recognitions received.")
    if "volunteer" in resume_text.lower():
        key_points.append("Include volunteer experiences.")
    if "communication" in resume_text.lower():
        key_points.append("Highlight your communication skills.")
    if "adaptability" in resume_text.lower():
        key_points.append(
            "Discuss your adaptability in changing environments.")
    if "software" in resume_text.lower():
        key_points.append("Mention your proficiency in specific software.")
    if "metrics" in resume_text.lower():
        key_points.append("Include metrics to quantify your achievements.")
    if "pressure" in resume_text.lower():
        key_points.append("Highlight your ability to work under pressure.")
    if "cross-functional" in resume_text.lower():
        key_points.append(
            "Discuss your experience with cross-functional teams.")
    if "strategic planning" in resume_text.lower():
        key_points.append("Mention your strategic planning skills.")
    if "budgeting" in resume_text.lower():
        key_points.append(
            "Include any experience with budgeting or financial management.")
    if "customer service" in resume_text.lower():
        key_points.append("Highlight your customer service skills.")
    if "data analysis" in resume_text.lower():
        key_points.append("Discuss your experience with data analysis.")
    if "mentoring" in resume_text.lower():
        key_points.append("Mention your ability to mentor or train others.")
    if "conflict resolution" in resume_text.lower():
        key_points.append("Include your experience with conflict resolution.")
    if "creativity" in resume_text.lower():
        key_points.append("Highlight your creativity and innovation.")
    if "technical writing" in resume_text.lower():
        key_points.append("Highlight your skills in technical writing.")

    return key_points


# This code display the Website Logo.
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
        # Android Developement tutorial
        "Add these Android Development course Certificates.": "https://youtu.be/HyU4vkZ2NB8?si=9bcQ0F1bsbpTUkv_",
        # Project Management tutorial
        "Highlight your leadership experiences.": "https://www.youtube.com/embed/JRlKKljzGI0?si=gkAXTgeC0BkclWK7",
        # Project Management tutorial
        "Include specific projects you've managed.": "https://www.youtube.com/watch?v=JrcjOCq7pLg",
        # How to list certifications
        "List relevant certifications.": "https://www.youtube.com/watch?v=m7103Kj6sSc",
        # Technical skills resume
        "Emphasize your technical skills.": "https://www.youtube.com/watch?v=366t4jL0b54",
        # Teamwork skills
        "Showcase your teamwork abilities.": "https://www.youtube.com/watch?v=wXWqYf4c97E",
        # Problem solving skills
        "Detail your problem-solving skills.": "https://www.youtube.com/watch?v=q6z3z45u-qQ",
        # How to add awards to resume
        "Mention any awards or recognitions received.": "https://www.youtube.com/watch?v=sO58z-V8V5Q",
        # Volunteer experience in resume
        "Include volunteer experiences.": "https://www.youtube.com/watch?v=j9uN9_4mD94",
        # communication skills
        "Highlight your communication skills.": "https://youtu.be/icudf_w_pqU?si=-gPm6TwMk6ckuHf8",
        # Adaptability skills
        "Discuss your adaptability in changing environments.": "https://www.youtube.com/watch?v=x74f6_g3zI0",
        # How to add software skills
        "Mention your proficiency in specific software.": "https://www.youtube.com/watch?v=W01xXh48uYk",
    }

    for point in key_points:
        if point in video_recommendations:
            with st.expander(f"{point} - Watch This Video"):
                st.video(video_recommendations[point])

        else:
            st.write(
                f"- {point}: Sorry, No specific video recommendations found for you")
            st.write("Have a Great day.")
