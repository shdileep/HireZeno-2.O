"""
=========================================================
HireZeno 2.O
Recruiter Dashboard
Author : HireZeno 2.O Team
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine
from core.hiring_score import HiringScoreEngine


def recruiter_dashboard_page():

    st.title("🎯 Recruiter Dashboard")

    st.markdown(
        "Enterprise dashboard for recruiters to evaluate candidates using AI."
    )

    engine = AIEngine()
    hiring = HiringScoreEngine()

    st.divider()

    # =====================================================
    # Candidate Inputs
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        ats = st.slider(
            "ATS Score",
            0,
            100,
            82,
            key="recruiter_ats"
        )

        similarity = st.slider(
            "Job Similarity",
            0,
            100,
            86,
            key="recruiter_similarity"
        )

    with col2:

        quality = st.slider(
            "Resume Quality",
            0,
            100,
            84,
            key="recruiter_quality"
        )

        experience = st.slider(
            "Experience",
            0,
            20,
            4,
            key="recruiter_experience"
        )

    matched = st.multiselect(

        "Matched Skills",

        [
            "Python",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "Power BI",
            "AWS",
            "Docker",
            "Excel",
        ],

        default=[
            "Python",
            "SQL",
            "Machine Learning",
        ],

        key="recruiter_matched"

    )

    missing = st.multiselect(

        "Missing Skills",

        [
            "AWS",
            "Docker",
            "Kubernetes",
            "Azure",
            "TensorFlow",
            "CI/CD",
        ],

        default=[
            "AWS",
            "Docker",
        ],

        key="recruiter_missing"

    )

    st.divider()

    # =====================================================
    # AI Evaluation
    # =====================================================

    if st.button(
        "🚀 Evaluate Candidate",
        use_container_width=True
    ):

        analytics = engine.analytics
        coach = engine.llm

        metrics = analytics.dashboard_metrics(

            ats=ats,

            similarity=similarity,

            quality=quality

        )

# Demo values for now.
# Later these will come from ML/DL modules.

        ml_score = quality
        dl_score = quality
        technical_score = quality
        soft_skill_score = 80
        experience_score = min(experience * 10, 100)

        hiring_report = hiring.report(

            ats=ats,

            similarity=similarity,

            ml=ml_score,

            dl=dl_score,

            technical=technical_score,

            soft_skills=soft_skill_score,

            experience=experience_score

        )

        report = coach.generate_report(

            ats=ats,

            similarity=similarity,

            quality=quality,

            experience=experience,

            matched=matched,

            missing=missing

        )

        # =============================================

        st.subheader("📊 Candidate Score")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "ATS",

            f"{ats}%"

        )

        c2.metric(

            "Similarity",

            f"{similarity}%"

        )

        c3.metric(

            "Hiring Score",

            f'{hiring_report["Hiring Score"]}%'

        )

        c4.metric(

            "Grade",

            hiring_report["Grade"]

        )

        st.progress(

            hiring_report["Hiring Score"] / 100

        )

        st.divider()

        # =============================================

        st.subheader("🎯 Recruiter Decision")

        st.success(

            hiring_report["Recommendation"]

        )

        st.info(

            report["Recruiter Decision"]

        )

        st.warning(

            f'Risk Level : {hiring_report["Risk"]}'

        )

        st.metric(

            "Hiring Probability",

            f'{hiring_report["Hiring Probability"]}%'

        )

        st.divider()

        # =============================================

        st.subheader("📋 AI Review")

        for item in report["AI Review"]:

            st.write(f"✅ {item}")

        st.divider()

        # =============================================

        st.subheader("📚 Recommended Learning")

        for skill in report["Learning Plan"]:

            st.write(f"• {skill}")

        st.divider()

        st.subheader("📄 Complete Report")

        st.json({

            "Analytics": metrics,

            "Hiring Report": hiring_report,

            "AI Review": report

        })
