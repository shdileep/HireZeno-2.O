"""
=========================================================
HireZeno 2.O
Enterprise ATS Analysis
Version : 11.0 Enterprise
Author : HireZeno 2.O Team
=========================================================
"""

import streamlit as st

from config import SUPPORTED_FILES

from core.resume_parser import ResumeParser
from core.keyword_engine import KeywordEngine
from core.ats_engine import ATSEngine
from core.hiring_score import HiringScoreEngine


def ats_analysis_page():

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
                <span class="score-badge">📊 ATS Engine Active</span>
                <span style="color: #64748b; font-size: 13px; font-weight: 600;">v12.0 Enterprise</span>
            </div>
            <h1 style="color: #0f172a; margin: 0 0 6px 0; font-size: 30px; font-weight: 800; letter-spacing: -0.6px;">
                Enterprise ATS Resume Analysis
            </h1>
            <p style="color: #64748b; font-size: 14px; margin: 0; font-weight: 500;">
                Upload your resume to receive an enterprise-grade ATS analysis with hiring score, recruiter insights, and skill-gap recommendations.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(

        "Upload Resume (PDF / DOCX)",

        type=SUPPORTED_FILES,

        key="ats_upload"

    )

    if uploaded_file is None:

        st.info("Please upload a resume.")

        return

    # =====================================================
    # Initialize Engines
    # =====================================================

    parser = ResumeParser()

    keyword_engine = KeywordEngine()

    ats_engine = ATSEngine()

    hiring = HiringScoreEngine()

    # =====================================================
    # Parse Resume
    # =====================================================

    with st.spinner("Parsing Resume..."):

        result = parser.analyze(

            uploaded_file

        )

    resume_text = result["raw_text"]

    st.success(

        "Resume parsed successfully."

    )

    st.divider()
    # =====================================================
    # ATS Analysis
    # =====================================================

    # KeywordEngine stores the master skills as a list.  ATSEngine expects the
    # parsed resume dictionary plus that list, and returns the complete ATS
    # report used throughout this page.
    report = ats_engine.analyze(

        result,

        keyword_engine.skills

    )

    ats_report = report

    experience_score = min(

        result.get("experience", 0) * 10,

        100

    )

    hiring_report = hiring.report(

        ats=report["ATS Score"],

        similarity=report["ATS Score"],

        ml=report["ATS Score"],

        dl=report["ATS Score"],

        technical=report["ATS Score"],

        soft_skills=80,

        experience=experience_score

    )

    st.success(

        "Enterprise ATS Analysis Completed Successfully."

    )

    st.divider()

    # =====================================================
    # Enterprise Dashboard
    # =====================================================

    st.subheader("📊 Enterprise ATS Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "ATS Score",

        f'{report["ATS Score"]}%'

    )

    c2.metric(

        "Hiring Score",

        f'{hiring_report["Hiring Score"]}%'

    )

    c3.metric(

        "Grade",

        hiring_report["Grade"]

    )

    c4.metric(

        "Probability",

        f'{hiring_report["Hiring Probability"]}%'

    )

    st.progress(

        hiring_report["Hiring Score"] / 100

    )

    st.divider()

    # =====================================================
    # Resume Statistics
    # =====================================================

    st.subheader("📈 Resume Statistics")

    s1, s2, s3, s4 = st.columns(4)

    s1.metric(

        "Words",

        result["word_count"]

    )

    s2.metric(

        "Skills",

        len(result["skills"])

    )

    s3.metric(

        "Experience",

        result.get("experience", 0)

    )

    s4.metric(

        "Projects",

        result.get("projects", 0)

    )

    st.divider()
    # =====================================================
    # Matched Skills
    # =====================================================

    st.subheader("✅ Matched Skills")

    matched = report.get("Matched Skills", [])

    if matched:

        cols = st.columns(4)

        for i, skill in enumerate(matched):

            cols[i % 4].success(skill)

    else:

        st.warning("No matched skills found.")

    st.divider()

    # =====================================================
    # Missing Skills
    # =====================================================

    st.subheader("❌ Missing Skills")

    missing = report.get("Missing Skills", [])

    if missing:

        cols = st.columns(4)

        for i, skill in enumerate(missing):

            cols[i % 4].error(skill)

    else:

        st.success("No missing skills detected.")

    st.divider()

    # =====================================================
    # Skill Gap Analysis
    # =====================================================

    st.subheader("📉 Skill Gap Analysis")

    st.metric(

        "Matched Skills",

        len(matched)

    )

    st.metric(

        "Missing Skills",

        len(missing)

    )

    if len(missing) == 0:

        st.success(

            "Excellent! Your resume covers all required skills."

        )

    else:

        st.warning(

            "Improve the missing skills to increase ATS compatibility."

        )

    st.divider()

    # =====================================================
    # Recruiter Recommendation
    # =====================================================

    st.subheader("🎯 Recruiter Recommendation")

    st.success(

        hiring_report["Recommendation"]

    )

    st.info(

        ats_report.get(

            "Recommendation",

            "No recommendation available."

        )

    )

    st.warning(

        f'Risk Level : {hiring_report["Risk"]}'

    )

    st.divider()

    # =====================================================
    # Career Recommendation
    # =====================================================

    st.subheader("📚 Recommended Learning")

    if missing:

        for skill in missing[:10]:

            st.write(f"• Learn **{skill}**")

    else:

        st.success(

            "Your skill profile is already strong."

        )

    st.divider()

    # =====================================================
    # Enterprise Report
    # =====================================================

    st.subheader("📄 Enterprise Analysis Report")

    st.json({

        "Resume Information": {

            "Name": result["name"],

            "Email": result["email"],

            "Phone": result["phone"],

            "Experience": result.get("experience", 0)

        },

        "ATS Report": report,

        "ATS Engine": ats_report,

        "Hiring Report": hiring_report

    })

    st.divider()

    st.caption(

        "HireZeno 2.O Enterprise Resume Intelligence Platform • Version 11.0"

    )
