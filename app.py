import streamlit as st
# PAGE CONFIGURATION
# ----------------------------------
st.set_page_config(
    page_title="Durga Prasad Annamdevula Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# ----------------------------------
# HOME SECTION
# ----------------------------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("DP profile.jpeg",width=220)

with col2:
    st.title("👨‍💻 Durga Prasad Annamdevula")
    st.subheader("AI & Cloud Enthusiast | Final Year Student")
    st.write("Recent Graduate And Fresher")

    st.write("""
    Welcome to my portfolio website.

    I am passionate about Artificial Intelligence, Machine Learning,
    Cloud Computing.
    I enjoy solving real-world problems through technology and building
    innovative solutions using AI and Cloud platforms.
    """)

st.markdown("---")

# ----------------------------------
# ABOUT ME
# ----------------------------------
st.header("🙋 About Me")

st.write("""
I am a final-year student with strong interest in Artificial Intelligence,
Machine Learning, Cloud Computing, and Software Development.

I enjoy working on practical projects that solve real-world problems and
continuously improve my technical skills through internships, certifications,
and hands-on learning.

Career Goal:
To build a successful career in AI, Machine Learning, Cloud Computing,
and Software Development while contributing to innovative technology solutions.

Technical Interests:
• Artificial Intelligence
• Machine Learning
• Cloud Computing
• Azure
• AWS
• Data Analytics
• NLP
• Computer Vision
""")

# ----------------------------------
# SKILLS
# ----------------------------------
st.header("💻 Skills")

skills_col1, skills_col2 = st.columns(2)

with skills_col:
    st.write("✅ Python")
    st.write("✅ Machine Learning")
    st.write("✅ Azure")
    st.write("✅ Artificial Intelligience")

# ----------------------------------
# PROJECTS
# ----------------------------------
st.header("🚀 Projects")

st.subheader("🌸 Iris Flower Classification")
st.write("""
Built a Machine Learning model using Scikit-learn to classify Iris flowers
based on petal and sepal measurements.
""")

st.subheader("📰 Fake News Detector For Students")
st.write("""
Developed a Natural Language Processing (NLP) based application that predicts
whether a news article is real or fake.
""")
st.write("Github Repository")
st.write("https://github.com/Annamdevula1/Fake-News-Detector-For-Students.git")

st.subheader("📊 Predicting Eligibility For NSAP Using ML")
st.write("""
Developed and deployed a Machine Learning model on IBM Cloud to predict
eligibility for the National Social Assistance Programme (NSAP).
""")
st.write("Github Repository")
st.write("https://github.com/Annamdevula1/PREDICTING-THE-ELIGIBILITY-FOR-NSAP-USING-ML.git")

st.subheader("🏦 Bank Fraud Detection System")
st.write("""
Developed a Machine Learning model to detect fraudulent bank transactions.
The system analyzes transaction data and classifies transactions as legitimate or fraudulent.
""")
st.write("Github Repository")
st.write("https://github.com/Annamdevula1/Bank-fraud-_detection-.git")
st.write("https://github.com/Annamdevula1/BANK-_-Fraud-.git")


# ----------------------------------
# INTERNSHIPS & CERTIFICATIONS
# ----------------------------------
st.header("🏆 Internships & Certifications")

st.subheader("Internships")

st.write("""
  ✅ Edunet Foundation + IBM SkillsBuild Artificial Intelligence Internship

  ✅ AICTE Internship Program

  ✅ AI & Cloud Emerging Technologies Internship
  ✅ AI Internship 
""")
st.subheader("Certifications")

st.write("""
✅ IBM SkillsBuild Certificate

✅ AICTE Internship Certificate

✅ Azure Certifications


""")

# ----------------------------------
# EDUCATION
# ----------------------------------
st.header("🎓 Education")

st.table({
    "Qualification": [
        "BCA",
        "Intermediate",
        "SSC (10th)"
    ],
    "Institution": [
        "Aditya Degree College, Rajamahendravaram",
        "Sasi Junior College Velivennu",
        "Bhashyam High School"
    ],
    "Score": [
        "8.97 CGPA",
        "9.20 CGPA",
        "10.00 CGPA"
    ]
})

st.subheader("Semester Wise Performance")

st.table({
    "Semester": [
        "Semester 1",
        "Semester 2",
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6"
    ],
    "SGPA": [
        "8.55",
        "9.12",
        "8.67",
        "9.14",
        "8.54",
        "10.00"
    ]
})

# ----------------------------------
# RESUME
# ----------------------------------
st.header("📄 Resume")

try:
    with open("Durga_Prasad_Resume.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Resume",
            data=pdf_file,
            file_name="Durga_Prasad_Resume.pdf",
            mime="application/pdf"
        )
except:
    st.info("Upload your resume PDF file to enable download.")

# ----------------------------------
# CONTACT SECTION
# ----------------------------------
st.header("📞 Contact")

st.write("📧 Email: durgaprasadannamdevula973@gmail.com")

st.write("🔗 LinkedIn:https://www.linkedin.com/in/durga-prasad-annamdevula-232538341")

st.write("💻 GitHub: https://github.com/Annamdevula1")

st.write("📱 Phone Number: +91 9618762533")

# ----------------------------------
# FOOTER
# ----------------------------------
st.markdown("---")
st.markdown(
    "<center><h5>© 2026 Durga Prasad Annamdevula | Portfolio Website</h5></center>",
    unsafe_allow_html=True
)
