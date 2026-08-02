"""
=========================================================
HireZeno 2.O
Enterprise NLP Resume Similarity Analysis
Version : 11.0 Enterprise
Author : HireZeno 2.O Team
=========================================================
"""

import streamlit as st

from core.similarity_engine import SimilarityEngine
from core.hiring_score import HiringScoreEngine


def nlp_analysis_page():

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
                <span class="score-badge">🧠 NLP Similarity Active</span>
                <span style="color: #64748b; font-size: 13px; font-weight: 600;">v12.0 Enterprise</span>
            </div>
            <h1 style="color: #0f172a; margin: 0 0 6px 0; font-size: 30px; font-weight: 800; letter-spacing: -0.6px;">
                Enterprise NLP Resume Similarity
            </h1>
            <p style="color: #64748b; font-size: 14px; margin: 0; font-weight: 500;">
                Compare a Resume with a Job Description using TF-IDF, Cosine Similarity and Enterprise Hiring Intelligence.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    resume = st.text_area(

        "📄 Resume Text",

        height=250,

        placeholder="Paste Resume Text Here..."

    )

    job = st.text_area(

        "💼 Job Description",

        height=250,

        placeholder="Paste Job Description Here..."

    )

    st.divider()

    if st.button(

        "🚀 Analyze Resume",

        use_container_width=True

    ):

        if resume.strip() == "" or job.strip() == "":

            st.warning(

                "Please provide both Resume and Job Description."

            )

            return

        similarity_engine = SimilarityEngine()

        hiring = HiringScoreEngine()

        with st.spinner(

            "Running Enterprise NLP Analysis..."

        ):

            report = similarity_engine.analyze(

                resume,

                job

            )

        similarity = report["Similarity Score"]

        hiring_report = hiring.report(

            ats=similarity,

            similarity=similarity,

            ml=similarity,

            dl=similarity,

            technical=similarity,

            soft_skills=80,

            experience=60

        )

        st.success(

            "Enterprise NLP Analysis Completed Successfully."

        )

        st.divider()
        # =====================================================
        # Enterprise Dashboard
        # =====================================================

        st.subheader("📊 Enterprise Similarity Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "Similarity Score",

            f"{similarity}%"

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
        # Similarity Summary
        # =====================================================

        st.subheader("📈 Similarity Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Resume Similarity",

                f"{similarity}%"

            )

            st.success(

                report["Grade"]

            )

        with col2:

            st.metric(

                "Risk Level",

                hiring_report["Risk"]

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
        # Detailed Analysis
        # =====================================================

        st.subheader("📄 Detailed Similarity Analysis")

        st.json(report)

        st.divider()

        # =====================================================
        # Skill Analysis
        # =====================================================

        st.subheader("🛠 Skill Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.write("### ✅ Matched Skills")

            matched = report.get("Matched Skills", [])

            if matched:

                for skill in matched:

                    st.success(skill)

            else:

                st.info("No matched skills found.")

        with col2:

            st.write("### ❌ Missing Skills")

            missing = report.get("Missing Skills", [])

            if missing:

                for skill in missing:

                    st.error(skill)

            else:

                st.success("No missing skills.")

        st.divider()

        # =====================================================
        # AI Interpretation
        # =====================================================

        st.subheader("🤖 AI Interpretation")

        if similarity >= 90:

            st.success(
                """
Excellent match.

Your resume is highly aligned with the Job Description.

Recruiters are likely to shortlist this profile.
"""
            )

        elif similarity >= 75:

            st.success(
                """
Strong match.

Only minor improvements are required before applying.
"""
            )

        elif similarity >= 60:

            st.warning(
                """
Moderate match.

Improve missing keywords and technical skills to increase ATS performance.
"""
            )

        elif similarity >= 40:

            st.warning(
                """
Low match.

Your resume needs additional optimization and relevant skills.
"""
            )

        else:

            st.error(
                """
Very poor match.

Rewrite your resume according to the Job Description before applying.
"""
            )

        st.divider()

        # =====================================================
        # Technology Stack
        # =====================================================

        st.subheader("⚙ Technology Used")

        st.dataframe(

            {

                "Component": [

                    "Vectorization",

                    "Similarity Metric",

                    "NLP Library",

                    "Enterprise Engine",

                    "Hiring Intelligence"

                ],

                "Technology": [

                    "TF-IDF",

                    "Cosine Similarity",

                    "Scikit-Learn",

                    "Similarity Engine v11",

                    "HiringScore Engine"

                ]

            },

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        # =====================================================
        # Enterprise JSON Report
        # =====================================================

        st.subheader("📑 Enterprise Report")

        st.json({

            "Similarity Report": report,

            "Hiring Report": hiring_report

        })

        st.divider()

        st.caption(

            "HireZeno 2.O Enterprise Resume Intelligence Platform • Version 11.0"

        )
