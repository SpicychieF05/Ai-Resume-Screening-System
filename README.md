# AI Powered Resume Screening System

## 📌 Project Name:
**AI Powered Resume Screening System**

## 📌 Project Description:
The **AI Powered Resume Screening System** is a **Streamlit-based web application** that helps **HR professionals and recruiters** efficiently screen resumes. It uses **Natural Language Processing (NLP) and Machine Learning (ML)** techniques to **extract, rank, and analyze** resumes based on a provided **job description**. The system also suggests **resume improvement tips** and provides **YouTube video recommendations** to help candidates optimize their resumes.

---

## 📂 Folder Structure:
```
AI_Powered_Resume_Screening_System/
│── logo_image/                     # Contains the logo image for UI
│── src/                             # Source code files
│   ├── app.py                       # Main Streamlit application
│   ├── resume_analyzer.py            # Resume analysis logic
│   ├── utils.py                      # Helper functions
│── data/                             # Sample resumes for testing
│── requirements.txt                   # List of dependencies
│── README.md                         # Project documentation
```

---

## 🚀 Installation and Setup Guide:

### Step 1: Clone the Repository
Open your terminal or command prompt and run:
```sh
git clone https://github.com/SpicychieF05/Ai-Resume-Screening-System
cd Ai-Resume-Screening-System
```

### Step 2: Create a Virtual Environment (Recommended)
For **Windows**:
```sh
python -m venv venv
venv\Scripts\activate
```
For **Mac/Linux**:
```sh
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies:
Run the following command to install required packages:
```sh
pip install -r requirements.txt
```

---

## ▶️ How to Run the Application:
Once dependencies are installed, start the application by running:
```sh
streamlit run app.py
```
This will open the **AI Powered Resume Screening System** in your default web browser.

---

## 🛠️ How It Works:
1. **Upload Resume** (PDF format only).
2. **Enter Job Description** in the text box.
3. **AI processes the resume**:
   - Extract text from the resume.
   - Compares it with the job description using **TF-IDF and Cosine Similarity**.
   - Ranks the resume based on similarity.
   - Provides **key improvement suggestions**.
4. **Resume Score is displayed** along with areas for improvement.
5. **YouTube video recommendations** are provided for skill enhancement.

---

## 🚀 Deployment:
- You can deploy the app on **Streamlit Cloud**, **Heroku**, or **AWS EC2**.
- Example deployment on Streamlit Cloud:
  ```sh
  streamlit share
  ```
- To deploy on **Heroku**:
  - Install Heroku CLI
  - Create `Procfile` with the following content:
    ```sh
    web: streamlit run app.py
    ```
  - Push the project to Heroku.

---

## 🔮 Future Scope:
- Improve resume parsing by integrating **spaCy** or **GPT-based NLP models**.
- Implement **AI-powered resume grading** with deeper insights.
- Add **multiple resume comparison** for bulk hiring.
- Extend support for **more file formats** like DOCX.
- **Automate job recommendations** based on resume analysis.

---

## 🏁 Conclusion:
The **AI Powered Resume Screening System** is a powerful tool designed to **streamline the recruitment process**. It automates **resume parsing, ranking, and analysis**, saving recruiters significant time and effort. Additionally, **job seekers** can benefit from **resume improvement suggestions** and **video recommendations**, making it easier to land their dream job.

This project is **open-source**, and contributions are welcome to further enhance its capabilities.
