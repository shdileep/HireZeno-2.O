"""
=========================================================
HireZeno 2.O
Executive Talent Intelligence Dashboard
Ultra-Professional Modern SaaS Edition (Clean Typography & Polished Layout)
Version : 12.0 Enterprise
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from config import (
    TOTAL_DEPARTMENTS,
    TOTAL_JOB_ROLES,
    TOTAL_SKILLS,
    TOTAL_AI_MODULES,
)


def dashboard_page():

    # ==========================================================
    # Global Executive SaaS CSS (Clean Inter / Plus Jakarta Sans)
    # ==========================================================

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

        /* Force pure white background and clean sans-serif font */
        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif !important;
            background-color: #f8fafc !important;
            color: #0f172a !important;
        }

        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2.5rem !important;
            max-width: 1280px !important;
        }

        /* Top Header Row */
        .exec-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 16px;
        }

        .exec-title h1 {
            color: #0f172a;
            font-size: 28px;
            font-weight: 800;
            letter-spacing: -0.6px;
            margin: 0 0 6px 0;
            line-height: 1.2;
        }

        .exec-title p {
            color: #64748b;
            font-size: 14px;
            margin: 0;
            font-weight: 500;
        }

        /* Status Badge Header Box */
        .status-box {
            background: #ffffff;
            border: 1px solid #eaecf0;
            border-radius: 14px;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            gap: 20px;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.04);
        }

        .status-label-title {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #94a3b8;
            margin-bottom: 4px;
        }

        .status-badges-group {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 12px;
            font-weight: 600;
            color: #334155;
        }

        .status-pill-active {
            background: #ecfdf5;
            color: #047857;
            border: 1px solid #a7f3d0;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .green-dot {
            width: 7px;
            height: 7px;
            background: #10b981;
            border-radius: 50%;
            display: inline-block;
        }

        /* Sleek Metric Cards */
        .metric-card {
            background: #ffffff;
            border: 1px solid #eaecf0;
            border-radius: 16px;
            padding: 20px 22px;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.05), 0 1px 2px rgba(16, 24, 40, 0.03);
            transition: all 0.25s ease;
            height: 100%;
        }

        .metric-card:hover {
            border-color: #3b82f6;
            box-shadow: 0 10px 20px -3px rgba(37, 99, 235, 0.08);
            transform: translateY(-2px);
        }

        .metric-card.accent-left {
            border-left: 4px solid #10b981;
        }

        .metric-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .metric-title {
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #64748b;
        }

        .metric-value {
            font-size: 30px;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.6px;
            margin-bottom: 6px;
            line-height: 1.1;
        }

        .metric-subtext {
            font-size: 12px;
            font-weight: 600;
            color: #2563eb;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .badge-blue {
            background: #eff6ff;
            color: #2563eb;
            border: 1px solid #dbeafe;
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
        }

        /* Main Section Container Card */
        .section-card {
            background: #ffffff;
            border: 1px solid #eaecf0;
            border-radius: 16px;
            padding: 22px 24px;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.05), 0 1px 2px rgba(16, 24, 40, 0.03);
            margin-bottom: 20px;
        }

        .section-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 18px;
            padding-bottom: 12px;
            border-bottom: 1px solid #f1f5f9;
        }

        .section-card-title {
            font-size: 14px;
            font-weight: 700;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .section-card-tags {
            font-size: 12px;
            font-weight: 600;
            color: #64748b;
        }

        /* Health Rows */
        .health-row-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid #f1f5f9;
        }

        .health-row-item:last-child {
            border-bottom: none;
        }

        .health-title {
            font-size: 13px;
            font-weight: 600;
            color: #334155;
        }

        .health-badge {
            background: #f8fafc;
            color: #2563eb;
            border: 1px solid #e2e8f0;
            padding: 3px 10px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
        }

        /* Capability List */
        .cap-row {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
            font-weight: 600;
            color: #334155;
            padding: 10px 0;
            border-bottom: 1px dashed #f1f5f9;
        }

        .cap-row:last-child {
            border-bottom: none;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ==========================================================
    # Top Executive Header
    # ==========================================================

    st.markdown(
        """
        <div class="exec-header">
            <div class="exec-title">
                <h1>Talent Intelligence Dashboard</h1>
                <p>Real-time AI recruitment analytics, automated candidate scoring, ATS parsing status, and neural model benchmarks.</p>
            </div>
            <div class="status-box">
                <div>
                    <div class="status-label-title">Engine Indicators</div>
                    <div class="status-badges-group">
                        <span>⚡ ATS</span>
                        <span>🧠 NLP</span>
                        <span>🤖 ML</span>
                        <span>🧬 Neural</span>
                    </div>
                </div>
                <div style="border-left: 1px solid #eaecf0; padding-left: 16px;">
                    <div class="status-label-title">US-East-Alpha</div>
                    <span class="status-pill-active">
                        <span class="green-dot"></span> Node Active
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ==========================================================
    # KPI Row (4 Clean Cards)
    # ==========================================================

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-card-header">
                    <span class="metric-title">Departments</span>
                    <span class="badge-blue">100%</span>
                </div>
                <div class="metric-value">{TOTAL_DEPARTMENTS}</div>
                <div class="metric-subtext">Active Coverage</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-card-header">
                    <span class="metric-title">Job Roles</span>
                    <span style="font-size: 16px;">⚙️</span>
                </div>
                <div class="metric-value">{TOTAL_JOB_ROLES}</div>
                <div class="metric-subtext" style="color: #64748b;">Benchmark Profiles</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-card-header">
                    <span class="metric-title">Skills Database</span>
                    <span style="font-size: 16px;">💡</span>
                </div>
                <div class="metric-value">{TOTAL_SKILLS:,}</div>
                <div class="metric-subtext" style="color: #64748b;">AI Taxonomies Indexed</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k4:
        st.markdown(
            f"""
            <div class="metric-card accent-left">
                <div class="metric-card-header">
                    <span class="metric-title">AI Modules</span>
                    <span style="color: #10b981; font-size: 16px;">✓</span>
                </div>
                <div class="metric-value">{TOTAL_AI_MODULES}</div>
                <div class="metric-subtext" style="color: #059669;">All Engines Live</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================================
    # Main Body Grid
    # ==========================================================

    col_chart, col_sidebar = st.columns([1.7, 1])

    with col_chart:
        st.markdown(
            """
            <div class="section-card">
                <div class="section-card-header">
                    <div class="section-card-title">
                        <span>📊 Analytics & Candidate Distribution</span>
                    </div>
                    <div class="section-card-tags">• Tech • Product • Design</div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        chart_df = pd.DataFrame(
            {
                "Category": [
                    "Highly Recommended",
                    "Recommended",
                    "Needs Review",
                    "Rejected",
                ],
                "Percentage": [42, 28, 58, 19],
            }
        )

        fig_bar = px.bar(
            chart_df,
            x="Category",
            y="Percentage",
            text="Percentage",
            color_discrete_sequence=["#3b82f6"],
        )

        fig_bar.update_traces(
            texttemplate="%{text}%",
            textposition="outside",
            marker_color="#3b82f6",
            marker_line_width=0,
            textfont=dict(color="#0f172a", size=13, weight="bold"),
        )

        fig_bar.update_layout(
            template="plotly_white",
            height=320,
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff",
            margin=dict(l=10, r=10, t=20, b=10),
            xaxis=dict(
                title="",
                showgrid=False,
                tickfont=dict(color="#334155", size=12, weight="bold"),
            ),
            yaxis=dict(
                title="",
                showgrid=True,
                gridcolor="#f1f5f9",
                showticklabels=False,
                range=[0, 70],
            ),
            font=dict(family="Plus Jakarta Sans, sans-serif"),
        )

        # Render Plotly chart without the floating modebar toolbar
        st.plotly_chart(
            fig_bar,
            use_container_width=True,
            config={"displayModeBar": False},
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col_sidebar:
        # Health Monitor Card
        st.markdown(
            """
            <div class="section-card">
                <div class="section-card-header">
                    <div class="section-card-title">
                        <span>🤖 AI Engine Health & Latency</span>
                    </div>
                </div>
                <div class="health-row-item">
                    <span class="health-title">Resume Parser Engine</span>
                    <span class="health-badge">12ms • 99.9%</span>
                </div>
                <div class="health-row-item">
                    <span class="health-title">ATS Matcher Engine</span>
                    <span class="health-badge">18ms • 100.0%</span>
                </div>
                <div class="health-row-item">
                    <span class="health-title">NLP Similarity Engine</span>
                    <span class="health-badge">24ms • 99.9%</span>
                </div>
                <div class="health-row-item">
                    <span class="health-title">XGBoost Predictor</span>
                    <span class="health-badge">15ms • 100.0%</span>
                </div>
                <div class="health-row-item">
                    <span class="health-title">Neural Evaluation Net</span>
                    <span class="health-badge">32ms • 99.7%</span>
                </div>
                <div class="health-row-item">
                    <span class="health-title">Executive Report Generator</span>
                    <span class="health-badge">45ms • 99.9%</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Core Capabilities Card
        st.markdown(
            """
            <div class="section-card">
                <div class="section-card-header">
                    <div class="section-card-title">
                        <span>Core Capabilities</span>
                    </div>
                </div>
                <div class="cap-row">
                    <span style="color: #2563eb;">✓</span> Automated Resume Parsing & Extraction
                </div>
                <div class="cap-row">
                    <span style="color: #2563eb;">✓</span> Weighted ATS Keyword Matching
                </div>
                <div class="cap-row">
                    <span style="color: #2563eb;">✓</span> TF-IDF Vector & Cosine Similarity
                </div>
                <div class="cap-row">
                    <span style="color: #2563eb;">✓</span> Neural Model Candidate Evaluation
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
