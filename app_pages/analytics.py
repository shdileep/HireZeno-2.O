"""
=========================================================
HireZeno 2.O
Enterprise Resume Analytics Dashboard
Author : HireZeno 2.O Team
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def analytics_page():

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
                <span class="score-badge">📈 EDA Analytics Engine Active</span>
                <span style="color: #64748b; font-size: 13px; font-weight: 600;">v12.0 Enterprise</span>
            </div>
            <h1 style="color: #0f172a; margin: 0 0 6px 0; font-size: 30px; font-weight: 800; letter-spacing: -0.6px;">
                Resume Analytics & EDA Dashboard
            </h1>
            <p style="color: #64748b; font-size: 14px; margin: 0; font-weight: 500;">
                Enterprise Resume Analytics powered by the AI Intelligence Engine.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    engine = AIEngine()

    st.divider()

    # =====================================================
    # Candidate Information
    # =====================================================

    st.subheader("Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            3,
            key="analytics_experience"
        )

        projects = st.number_input(
            "Projects",
            0,
            50,
            5,
            key="analytics_projects"
        )

        certifications = st.number_input(
            "Certifications",
            0,
            20,
            2,
            key="analytics_certifications"
        )

    with col2:

        resume_words = st.number_input(
            "Resume Word Count",
            100,
            5000,
            600,
            key="analytics_words"
        )

        resume_score = st.slider(
            "Resume Quality Score",
            0,
            100,
            80,
            key="analytics_score"
        )

    st.divider()

    # =====================================================
    # Skill Analysis
    # =====================================================

    st.subheader("Skill Analysis")

    matched = st.multiselect(

        "Matched Skills",

        [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "Deep Learning",
            "Power BI",
            "Excel",
            "AWS",
            "Docker",
        ],

        default=[
            "Python",
            "SQL",
            "Machine Learning",
        ],

        key="analytics_matched"

    )

    missing = st.multiselect(

        "Missing Skills",

        [
            "AWS",
            "Docker",
            "Kubernetes",
            "CI/CD",
            "TensorFlow",
            "Power BI",
            "Azure",
        ],

        default=[
            "AWS",
            "Docker",
        ],

        key="analytics_missing"

    )

    st.divider()

    # =====================================================
    # Generate Analytics
    # =====================================================

    if st.button(
        "🚀 Generate Analytics",
        use_container_width=True
    ):

        analytics = engine.analytics

        features = {

            "Experience": experience,

            "Projects": projects,

            "Certifications": certifications,

            "Resume Words": resume_words,

            "Resume Quality Score": resume_score

        }

        # ------------------------------------------------

        st.subheader("📋 Resume Summary")

        summary = analytics.summary(features)

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------------

        st.subheader("🛠 Skill Distribution")

        skill_df = analytics.skill_distribution(
            matched,
            missing
        )

        st.dataframe(
            skill_df,
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------------

        pie = analytics.pie_chart(
            matched,
            missing
        )

        st.plotly_chart(
            pie,
            use_container_width=True,
            key="analytics_pie"
        )

        # ------------------------------------------------

        bar = analytics.bar_chart(
            matched,
            missing
        )

        st.plotly_chart(
            bar,
            use_container_width=True,
            key="analytics_bar"
        )

        st.divider()

        # =====================================================
        # Analytics Metrics
        # =====================================================

        st.subheader("📊 Analytics Metrics")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Experience Level",
            analytics.experience_level(experience)
        )

        c2.metric(
            "Resume Strength",
            analytics.resume_strength(resume_score)
        )

        c3.metric(
            "Matched Skills",
            len(matched)
        )

        st.divider()

        # =====================================================
        # Dashboard Metrics
        # =====================================================

        metrics = analytics.dashboard_metrics(

            ats=resume_score,

            similarity=85,

            quality=resume_score

        )

        st.subheader("📈 Dashboard Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Overall Score",
            metrics["Overall Score"]
        )

        col2.metric(
            "Grade",
            metrics["Grade"]
        )

        col3.metric(
            "Recommendation",
            metrics["Recommendation"]
        )

        st.divider()

        st.json(metrics)
