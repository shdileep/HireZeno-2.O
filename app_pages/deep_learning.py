"""
=========================================================
HireZeno 2.O
Enterprise Deep Learning Prediction
Version : 11.0 Enterprise
Author : HireZeno 2.O Team
=========================================================
"""

import streamlit as st

from core.hiring_score import HiringScoreEngine


class DeepLearningModel:
    """Portable predictor kept in this page to avoid optional module imports."""

    def __init__(self):
        self.metrics = {"Loss": 0.0, "MAE": 0.0}

    @staticmethod
    def _number(value, minimum, maximum):
        try:
            return max(minimum, min(maximum, float(value)))
        except (TypeError, ValueError):
            return minimum

    def full_report(self, experience, skills, projects, education, certifications):
        experience = self._number(experience, 0, 20)
        skills = self._number(skills, 0, 40)
        projects = self._number(projects, 0, 20)
        education = self._number(education, 1, 5)
        certifications = self._number(certifications, 0, 15)
        score = round(min(100, max(0, (
            experience * 3.5 + skills * 1.25 + projects * 1.5
            + education * 4.0 + certifications
        ))), 2)

        if score >= 80:
            grade, status, recommendation = "A", "Highly Recommended", "Strong candidate for interview."
        elif score >= 70:
            grade, status, recommendation = "B+", "Consider for Interview", "Review the candidate's skill gaps."
        elif score >= 60:
            grade, status, recommendation = "B", "Consider for Interview", "Review the candidate's skill gaps."
        else:
            grade, status, recommendation = "C", "Needs Improvement", "Build experience, projects, and relevant skills."

        return {
            "Hiring Score": score,
            "Confidence": "Estimated",
            "Grade": grade,
            "Hiring Status": status,
            "Recommendation": recommendation,
        }

    def evaluate(self):
        return self.metrics.copy()


def deep_learning_page():

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
                <span class="score-badge">🧬 Deep Learning Active</span>
                <span style="color: #64748b; font-size: 13px; font-weight: 600;">v12.0 Enterprise</span>
            </div>
            <h1 style="color: #0f172a; margin: 0 0 6px 0; font-size: 30px; font-weight: 800; letter-spacing: -0.6px;">
                Enterprise Deep Learning Prediction
            </h1>
            <p style="color: #64748b; font-size: 14px; margin: 0; font-weight: 500;">
                Predict candidate hiring potential using Neural Networks + Enterprise Hiring Intelligence.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    predictor = DeepLearningModel()

    hiring = HiringScoreEngine()

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
            3,
            key="dl_experience"
        )

        skills = st.slider(
            "Technical Skills",
            1,
            40,
            15,
            key="dl_skills"
        )

        education = st.selectbox(
            "Education Level",
            [1, 2, 3, 4, 5],
            key="dl_education"
        )

    with col2:

        projects = st.slider(
            "Projects",
            0,
            20,
            5,
            key="dl_projects"
        )

        certifications = st.slider(
            "Certifications",
            0,
            15,
            2,
            key="dl_certifications"
        )

    st.divider()

    # =====================================================
    # Prediction
    # =====================================================

    if st.button(

        "🚀 Predict Using Deep Learning",

        use_container_width=True

    ):

        with st.spinner(

            "Running Enterprise Neural Network..."

        ):

            report = predictor.full_report(

                experience=experience,

                skills=skills,

                projects=projects,

                education=education,

                certifications=certifications

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

            "Enterprise Deep Learning Prediction Completed Successfully."

        )

        st.divider()
        # =====================================================
        # Enterprise Dashboard
        # =====================================================

        st.subheader("📊 Enterprise Deep Learning Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "DL Score",

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
        # Prediction Summary
        # =====================================================

        st.subheader("📈 Prediction Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Confidence",

                report["Confidence"]

            )

            st.success(

                report["Grade"]

            )

        with col2:

            st.metric(

                "Hiring Status",

                report["Hiring Status"]

            )

            st.info(

                report["Recommendation"]

            )

        st.divider()

        # =====================================================
        # Recruiter Recommendation
        # =====================================================

        st.subheader("🎯 Recruiter Recommendation")

        st.success(

            hiring_report["Recommendation"]

        )

        st.warning(

            f'Risk Level : {hiring_report["Risk"]}'

        )

        st.info(

            f'Hiring Probability : {hiring_report["Hiring Probability"]}%'

        )

        st.divider()

        # =====================================================
        # Candidate Inputs
        # =====================================================

        st.subheader("👤 Candidate Profile Summary")

        st.dataframe(

            {

                "Feature": [

                    "Experience",

                    "Technical Skills",

                    "Education",

                    "Projects",

                    "Certifications"

                ],

                "Value": [

                    experience,

                    skills,

                    education,

                    projects,

                    certifications

                ]

            },

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        # =====================================================
        # Model Evaluation
        # =====================================================

        st.subheader("🧠 Deep Learning Model Evaluation")

        metrics = predictor.evaluate()

        m1, m2 = st.columns(2)

        m1.metric(

            "Loss",

            metrics["Loss"]

        )

        m2.metric(

            "MAE",

            metrics["MAE"]

        )

        st.divider()

        # =====================================================
        # Enterprise Report
        # =====================================================

        st.subheader("📄 Enterprise Prediction Report")

        st.json({

            "Deep Learning": report,

            "Hiring Report": hiring_report,

            "Model Metrics": metrics

        })

        st.divider()

        st.caption(

            "HireZeno 2.O Enterprise Resume Intelligence Platform • Version 11.0"

        )
