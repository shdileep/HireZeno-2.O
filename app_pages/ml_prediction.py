"""
=========================================================
HireZeno 2.O
Enterprise Machine Learning Prediction
Version : 11.0 Enterprise
Author : HireZeno 2.O Team
=========================================================
"""

import streamlit as st

from core.ai_engine import AIEngine
from core.hiring_score import HiringScoreEngine


def ml_prediction_page():

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
                <span class="score-badge">🤖 ML Prediction Active</span>
                <span style="color: #64748b; font-size: 13px; font-weight: 600;">v12.0 Enterprise</span>
            </div>
            <h1 style="color: #0f172a; margin: 0 0 6px 0; font-size: 30px; font-weight: 800; letter-spacing: -0.6px;">
                Enterprise Machine Learning Prediction
            </h1>
            <p style="color: #64748b; font-size: 14px; margin: 0; font-weight: 500;">
                Predict candidate hiring potential using Machine Learning + Enterprise Hiring Intelligence.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    engine = AIEngine()

    hiring = HiringScoreEngine()

    # =====================================================
    # Train ML Models
    # =====================================================

    with st.spinner("Training Enterprise ML Models..."):

        comparison = engine.ml.train_models()

    st.subheader("📊 Model Performance Comparison")

    st.dataframe(

        comparison,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Candidate Profile
    # =====================================================

    st.subheader("👤 Candidate Profile")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(

            "Experience (Years)",

            0,

            20,

            3

        )

        skills = st.slider(

            "Technical Skills",

            1,

            40,

            15

        )

        education = st.selectbox(

            "Education Level",

            [

                1,

                2,

                3,

                4,

                5

            ]

        )

    with col2:

        projects = st.slider(

            "Projects",

            0,

            20,

            5

        )

        certifications = st.slider(

            "Certifications",

            0,

            15,

            2

        )

        model = st.selectbox(

            "Prediction Model",

            comparison["Model"].tolist()

        )

    st.divider()

    # =====================================================
    # Predict
    # =====================================================

    if st.button(

        "🚀 Predict Hiring Score",

        use_container_width=True

    ):

        with st.spinner(

            "Running Enterprise ML Prediction..."

        ):

            report = engine.ml.full_report(

                experience=experience,

                skills=skills,

                education=education,

                projects=projects,

                certifications=certifications,

                model_name=model

            )

        score = report["Hiring Score"]

        hiring_report = hiring.report(

            ats=score,

            similarity=score,

            ml=score,

            dl=score,

            technical=skills * 2.5,

            soft_skills=80,

            experience=min(

                experience * 10,

                100

            )

        )

        st.success(

            "Enterprise Prediction Completed Successfully."

        )

        st.divider()
        # =====================================================
        # Enterprise Dashboard
        # =====================================================

        st.subheader("📊 Enterprise Hiring Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "ML Score",

            f"{score}%"

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

            "Hiring Probability",

            f'{hiring_report["Hiring Probability"]}%'

        )

        st.progress(

            hiring_report["Hiring Score"] / 100

        )

        st.divider()

        # =====================================================
        # Candidate Summary
        # =====================================================

        st.subheader("👤 Candidate Summary")

        s1, s2, s3 = st.columns(3)

        s1.metric(

            "Experience",

            f"{experience} Years"

        )

        s2.metric(

            "Technical Skills",

            skills

        )

        s3.metric(

            "Projects",

            projects

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

            report["Recommendation"]

        )

        st.warning(

            f'Risk Level : {hiring_report["Risk"]}'

        )

        st.divider()

        # =====================================================
        # Prediction Summary
        # =====================================================

        st.subheader("📈 Machine Learning Prediction Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Predicted Hiring Score",

                f"{score}%"

            )

            st.success(

                report["Grade"]

            )

        with col2:

            st.metric(

                "Hiring Probability",

                f'{hiring_report["Hiring Probability"]}%'

            )

            st.info(

                hiring_report["Recommendation"]

            )

        st.divider()

        # =====================================================
        # Candidate Input Summary
        # =====================================================

        st.subheader("📋 Candidate Inputs")

        st.dataframe(

            {

                "Feature": [

                    "Experience",

                    "Technical Skills",

                    "Education",

                    "Projects",

                    "Certifications",

                    "Prediction Model"

                ],

                "Value": [

                    experience,

                    skills,

                    education,

                    projects,

                    certifications,

                    model

                ]

            },

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        # =====================================================
        # Enterprise JSON Report
        # =====================================================

        st.subheader("📄 Enterprise Prediction Report")

        st.json({

            "Machine Learning": report,

            "Hiring Report": hiring_report

        })

        st.divider()

        st.caption(

            "HireZeno 2.O Enterprise Resume Intelligence Platform • Version 11.0"

        )
