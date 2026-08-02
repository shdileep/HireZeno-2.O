"""
=========================================================
HireZeno 2.O / HireZeno 2.O
Enterprise Resume Analyzer (Billion-Dollar Executive SaaS UI)
Version : 12.0 Enterprise
=========================================================
"""

import streamlit as st
from config import SUPPORTED_FILES
from core.resume_parser import ResumeParser


def resume_analyzer_page():

    # ==========================================================
    # Global Executive SaaS CSS
    # ==========================================================
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
        }

        .saas-hero-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 60%, #eff6ff 100%);
            border: 1px solid #eaecf0;
            border-radius: 20px;
            padding: 24px 28px;
            box-shadow: 0 1px 4px rgba(16,24,40,0.04);
            margin-bottom: 20px;
        }

        .saas-card {
            background: #ffffff;
            border: 1px solid #eaecf0;
            border-radius: 16px;
            padding: 20px 22px;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
            margin-bottom: 16px;
        }

        .skill-pill {
            background: #f0fdf4;
            color: #15803d;
            border: 1px solid #bbf7d0;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            display: inline-block;
            margin: 4px;
        }

        .score-badge {
            background: #eff6ff;
            color: #1d4ed8;
            border: 1px solid #bfdbfe;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="saas-hero-card">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <span class="score-badge">📄 AI Engine Active</span>
                <span style="color: #64748b; font-size: 13px; font-weight: 600;">v12.0 Enterprise</span>
            </div>
            <h1 style="color: #0f172a; margin: 0 0 6px 0; font-size: 30px; font-weight: 800; letter-spacing: -0.6px;">
                Enterprise Resume Analyzer
            </h1>
            <p style="color: #64748b; font-size: 14px; margin: 0; font-weight: 500;">
                Upload your resume and receive a complete AI-powered ATS analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF / DOCX)",
        type=SUPPORTED_FILES,
        key="resume_upload"
    )

    if uploaded_file is None:
        st.info("Upload a resume to start analysis.")
        return

    parser = ResumeParser()

    with st.spinner("Analyzing Resume..."):
        try:
            result = parser.analyze(uploaded_file)
        except Exception as e:
            import traceback
            st.code(traceback.format_exc())
            st.stop()

        st.success("Resume analyzed successfully.")

    # ===================================================
    # Candidate Summary Card
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-top: 16px; margin-bottom: 12px;">
            🎓 Candidate Summary
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Experience",
            f'{result["experience"]} Years'
        )

    education = ", ".join(result["education"]) if result["education"] else "-"

    with c2:
        st.metric(
            "Education",
            education
        )

    with c3:
        st.metric(
            "Projects",
            result["projects"]
        )

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(result["name"])
        st.write("📧", result["email"])
        st.write("📱", result["phone"])

    with col2:
        score = result["resume_score"]
        if score >= 90:
            grade = "A+"
            color = "🟢"
        elif score >= 80:
            grade = "A"
            color = "🟢"
        elif score >= 70:
            grade = "B+"
            color = "🟡"
        elif score >= 60:
            grade = "B"
            color = "🟠"
        else:
            grade = "C"
            color = "🔴"

        st.metric("ATS Score", f"{score}%")
        st.metric("Grade", f"{color} {grade}")

    st.divider()

    # ===================================================
    # Resume Statistics
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;">
            📊 Resume Statistics
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Words", result["word_count"])
    c2.metric("Characters", result["character_count"])
    c3.metric("Lines", result["line_count"])
    c4.metric("Reading Time", f'{result["reading_time"]} min')

    st.divider()

    # ===================================================
    # Skills
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;">
            🛠 Skills Detected
        </div>
        """,
        unsafe_allow_html=True,
    )

    skills = result["skills"]

    if skills:
        cols = st.columns(4)
        for i, skill in enumerate(skills):
            cols[i % 4].success(skill)
    else:
        st.warning("No skills detected.")

    st.divider()

    # ===================================================
    # Links
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;">
            🌐 Professional Profiles
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("LinkedIn :", result["linkedin"] or "-")
    st.write("GitHub :", result["github"] or "-")

    if result["portfolio"]:
        st.write("Portfolio")
        for site in result["portfolio"]:
            st.write("•", site)

    st.divider()

    # ===================================================
    # ATS Feedback
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;">
            🤖 AI ATS Review
        </div>
        """,
        unsafe_allow_html=True,
    )

    if score >= 90:
        st.success(
            """
Excellent ATS optimized resume.

Strong keyword coverage.

Well formatted for recruiters.
"""
        )
    elif score >= 75:
        st.info(
            """
Good resume.

Add more measurable achievements.

Improve technical keywords.
"""
        )
    else:
        st.error(
            """
Resume requires improvement.

• Add projects

• Add certifications

• Improve formatting

• Improve ATS keywords

• Add measurable achievements
"""
        )

    st.divider()

    # ===================================================
    # Resume Preview
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;">
            📄 Resume Preview
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.text_area(
        "",
        result["raw_text"],
        height=350
    )

    st.divider()

    # ===================================================
    # Final Recommendation
    # ===================================================

    st.markdown(
        """
        <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 12px;">
            🎯 Recruiter Recommendation
        </div>
        """,
        unsafe_allow_html=True,
    )

    if score >= 90:
        st.success("Highly Recommended")
    elif score >= 75:
        st.info("Recommended")
    elif score >= 60:
        st.warning("Needs Improvement")
    else:
        st.error("Not Recommended")

    st.divider()

    st.caption("HireZeno 2.O Resume Intelligence Platform • Version 10 Enterprise")
