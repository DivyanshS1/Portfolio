import streamlit as st
from PIL import Image
import qrcode

# ================= Page Config ==================
st.set_page_config(
    page_title="Divyansh Singhal Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# ================= Custom CSS ==================
st.markdown("""
    <style>
        /* Background */
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Headings */
        h1, h2, h3 {
            color: #00c6ff;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 40px 20px;
        }
        .hero h1 {
            font-size: 56px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .hero h3 {
            font-size: 22px;
            font-weight: normal;
            color: #dcdcdc;
        }

        /* Buttons */
        .stDownloadButton button {
            background: #00c6ff;
            color: black;
            border-radius: 25px;
            padding: 8px 20px;
            font-weight: bold;
        }
        .stDownloadButton button:hover {
            background: #0084ff;
            color: white;
        }

        /* Cards */
        .card {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            transition: 0.3s;
        }
        .card:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-5px);
        }
        .card h4 {
            color: #00c6ff;
        }

        /* Contact */
        .contact {
            font-size: 18px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 12px;
        }

        /* Links */
        a {
            color: #00c6ff !important;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ================= Hero Section ==================
st.markdown("""
<div class='hero'>
    <h1>👨‍💻 Divyansh Singhal</h1>
    <h3>App Developer | ML Enthusiast | React Developer</h3>
    <p>📍 Noida, India</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    # QR Code
    portfolio_link = "https://drive.google.com/file/d/1Wl63892xXj8bwNMxibqTLsN6m5B_GGW8/view?usp=drive_link"
    qr = qrcode.make(portfolio_link)
    qr.save("qr.png")
    st.image("qr.png", width=140, caption="Scan for Portfolio")

with col2:
    with open("Divyansh_Resume.pdf", "rb") as f:
        st.download_button("📄 Download My Resume", f, file_name="Divyansh_Singhal_Resume.pdf")

# ================= Links ==================
st.markdown("## 🔗 Connect with Me")
cols = st.columns(4)
cols[0].markdown("[🌐 GitHub](https://github.com/DivyanshS1)")
cols[1].markdown("[💼 LinkedIn](https://www.linkedin.com/in/divyanshsinghal)")
cols[2].markdown("[🧩 LeetCode](https://leetcode.com/u/divyanshS1/)")
cols[3].markdown("[📘 GeeksforGeeks](https://www.geeksforgeeks.org/user/singhaldivw7f1/)")

# ================= Profile ==================
st.markdown("## 🧾 Profile Summary")
st.markdown("""
<div class='card'>
App Developer & Machine Learning Enthusiast with experience in Flutter, Firebase, ReactJS, and on-device ML.  
🚀 Published 3+ apps on Google Play Store  
📜 Granted a UK Patent  
🎤 Presented research at an international conference  
</div>
""", unsafe_allow_html=True)

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
    st.markdown(f"<b>{skill}</b>", unsafe_allow_html=True)
    st.progress(val)

# ================= Experience ==================
st.markdown("## 💼 Experience")

st.markdown("""
<div class='card'>
    <h4>ReactJS Intern | MS Technologies (Apr 2025 – Jun 2025)</h4>
    <p>Developed Employee Leave Management System using ReactJS.</p>
    <a href='https://drive.google.com/file/d/1f27KU7jDLzxc5k4FM-mv8So4vfa5MtOX/view?usp=sharing'>📜 Certificate</a>
</div>
<div class='card'>
    <h4>ML & App Dev Intern | KIIT (Apr 2024 – Jul 2024)</h4>
    <p>Integrated Firebase backend, real-time DB & implemented TFLite models.</p>
    <a href='https://drive.google.com/file/d/1tNBgTAQFdWEgfnJYYGr3_HC_49RnxZf-/view?usp=sharing'>📜 Certificate</a>
</div>
""", unsafe_allow_html=True)

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
for p in projects:
    st.markdown(f"""
    <div class='card'>
        <h4>{p['name']}</h4>
        <p>{p['desc']}</p>
        <a href='{p['link']}'>🔗 Play Store Link</a>
    </div>
    """, unsafe_allow_html=True)

# ================= Patents & Research ==================
st.markdown("## 🏅 Patents & Research")
st.markdown("""
<div class='card'>
<b>UK Patent (Feb 2025):</b> Device for Tracking Cancer Patient Movement during Radiotherapy.  
<a href='https://drive.google.com/file/d/1n8BSOZJM6vTN6_RDoKyxSOE3_BML5X4s/view?usp=sharing'>📜 Certificate</a>
</div>
<div class='card'>
<b>Research (ISMS 2025):</b> Feedback-Driven Continuous Learning in RAG Systems.  
<a href='https://drive.google.com/file/d/1Q3eiaXtjYKn-klHW1IPLaM2jfkaP5KU_/view?usp=sharing'>📜 Certificate</a> | 
<a href='https://credsverse.com/credentials/86ac5dd2-37a8-4392-956a-dfb2dccbbd9e'>✅ Verify Credential</a>
</div>
""", unsafe_allow_html=True)

# ================= Achievements ==================
st.markdown("## 🏆 Achievements")
st.markdown("""
<div class='card'>
- 🚀 Published 3+ apps on Google Play Store  
- 📈 Paper Quest App crossed **1000+ downloads**
</div>
""", unsafe_allow_html=True)

# ================= Contact ==================
st.markdown("## 📬 Contact Me")
st.markdown("""
<div class='contact'>
📧 <b>Email:</b> singhaldivyansh220@gmail.com <br>
📞 <b>Phone:</b> +91 8368135283
</div>
""", unsafe_allow_html=True)
