import streamlit as st
from PIL import Image
import qrcode

# ================= Header ==================
st.set_page_config(page_title="Divyansh Singhal Portfolio", page_icon="👨‍💻", layout="wide")

st.title("👨‍💻 Divyansh Singhal")
st.subheader("App Developer | ML Enthusiast | React Developer")
st.write("📍 Noida, India")

# QR Code for portfolio link
portfolio_link = "https://YOUR-PORTFOLIO-LINK.com"
qr = qrcode.make(portfolio_link)
qr.save("qr.png")
st.image("qr.png", width=120)

# Resume Download
with open("Divyansh_Resume.pdf", "rb") as f:
    st.download_button("📄 Download My Resume", f, file_name="Divyansh_Singhal_Resume.pdf")

# ================= Links ==================
st.markdown("### 🔗 Connect with Me")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("[GitHub](https://github.com/DivyanshS1)")
with col2:
    st.markdown("[LinkedIn](https://www.linkedin.com/in/divyanshsinghal)")
with col3:
    st.markdown("[LeetCode](https://leetcode.com/u/divyanshS1/)")
with col4:
    st.markdown("[GeeksforGeeks](https://www.geeksforgeeks.org/user/singhaldivw7f1/)")

# ================= About ==================
st.markdown("## 🧾 Profile Summary")
st.write("""
App Developer & Machine Learning Enthusiast with experience in Flutter, Firebase, ReactJS, and on-device ML.
Published 3+ apps on Google Play Store, granted a UK Patent, and presented research at an international conference.
""")

# ================= Skills ==================
st.markdown("## 💻 Technical Skills")
skills = {
    "Flutter & Dart": 90,
    "Firebase": 85,
    "ReactJS": 80,
    "Java": 85,
    "Machine Learning (TFLite)": 75
}
for skill, val in skills.items():
    st.progress(val)
    st.text(f"{skill} - {val}%")

# ================= Education ==================
st.markdown("## 🎓 Education")
st.write("**B.Tech, Computer Science & Engineering** - KIIT, Bhubaneswar (Expected 2027)")
st.write("CGPA: 9.33/10")

# ================= Experience ==================
st.markdown("## 💼 Experience")
st.write("### ReactJS Intern | MS Technologies (Apr 2025 – Jun 2025)")
st.write("Developed Employee Leave Management System using ReactJS.")
st.markdown("[Certificate](https://drive.google.com/file/d/1f27KU7jDLzxc5k4FM-mv8So4vfa5MtOX/view?usp=sharing)")

st.write("### ML & App Dev Intern | KIIT (Apr 2024 – Jul 2024)")
st.write("Integrated Firebase backend, real-time DB & implemented TFLite models.")
st.markdown("[Certificate](https://drive.google.com/file/d/1tNBgTAQFdWEgfnJYYGr3_HC_49RnxZf-/view?usp=sharing)")

# ================= Projects ==================
st.markdown("## 🚀 Projects")
projects = [
    {
        "name": "Paper Quest App",
        "desc": "Student-centric past paper repository with real-time storage & rewards.",
        "link": "https://play.google.com/store/apps/details?id=org.div.pyq_app&pcampaignid=web_share"
    },
    {
        "name": "Image Classifier App",
        "desc": "Mobile-based image recognition using MobileNet + TFLite.",
        "link": "https://play.google.com/store/apps/details?id=org.div.image_classifier&pcampaignid=web_share"
    },
    {
        "name": "Hostel Owner App",
        "desc": "Hostel management app for attendance & fee tracking.",
        "link": "#"
    }
]

for project in projects:
    st.markdown(f"**{project['name']}**")
    st.write(project['desc'])
    st.markdown(f"[Play Store Link]({project['link']})")
    st.write("---")

# ================= Patents & Research ==================
st.markdown("## 🏅 Patents & Research")
st.write("**UK Patent (Feb 2025):** Device for Tracking Cancer Patient Movement during Radiotherapy.")
st.markdown("[Certificate](https://drive.google.com/file/d/1n8BSOZJM6vTN6_RDoKyxSOE3_BML5X4s/view?usp=sharing)")

st.write("**Research:** Feedback-Driven Continuous Learning in RAG Systems (ISMS 2025).")
st.markdown("[Certificate](https://drive.google.com/file/d/1Q3eiaXtjYKn-klHW1IPLaM2jfkaP5KU_/view?usp=sharing) | [Verify Credential](https://credsverse.com/credentials/86ac5dd2-37a8-4392-956a-dfb2dccbbd9e)")

# ================= Achievements ==================
st.markdown("## 🏆 Achievements")
st.write("- Published 3+ apps on Google Play Store")
st.write("- Paper Quest App crossed 1000+ downloads")

# ================= Contact ==================
st.markdown("## 📬 Contact Me")
st.write("📧 Email: singhaldivyansh220@gmail.com")
st.write("📞 Phone: +91 8368135283")
