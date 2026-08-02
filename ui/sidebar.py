"""
=========================================================
HireZeno 2.0
Stitch Screen Light Theme Sidebar Navigation
=========================================================
"""

import streamlit as st
import urllib.parse
from config import SIDEBAR_MENU, APP_VERSION

LOGO_URL = "https://lh3.googleusercontent.com/aida-public/AB6AXuDH1iUb0dRJ3NRiZbdcttG01YPuipMdgWLw1H8pR096uShERPhpSZ46J64JbI_Y-dYZvBjJCwaAO9-KPjnWhxiV0GqPI1fYckK8orYTYnTqqk3YMY72E7pfS1klf6TDCFWJ5mwW6jjy8L3Ecxkr4BEi5HolrD7dSn_lVvimBzceq86YQEfY3hyQ6WsHq5aEQBZzFQv3AazvwJtocOmZBAxai2T1MOCkd56qG84p1bAcoVkLMD7jt733ZObJEl6C2XMw0sY"

MENU_ITEMS_SPEC = [
    ("Dashboard", "dashboard", "🏠 Dashboard"),
    ("Resume Analyzer", "description", "📄 Resume Analyzer"),
    ("ATS Analysis", "analytics", "📊 ATS Analysis"),
    ("NLP Analysis", "psychology", "🧠 NLP Analysis"),
    ("EDA Dashboard", "leaderboard", "📈 EDA Dashboard"),
    ("Machine Learning", "memory", "🤖 Machine Learning"),
    ("Deep Learning", "hub", "🧬 Deep Learning"),
    ("Recruiter Dashboard", "work", "🎯 Recruiter Dashboard"),
    ("Salary Prediction", "payments", "💼 Salary Prediction"),
    ("Learning Roadmap", "map", "📚 Learning Roadmap"),
    ("AI Career Coach", "smart_toy", "💬 AI Career Coach"),
    ("Interview Generator", "question_answer", "🎤 Interview Generator"),
    ("Cover Letter", "mail", "📜 Cover Letter"),
    ("Email Generator", "forward_to_inbox", "📧 Email Generator"),
    ("LinkedIn Optimizer", "share", "👤 LinkedIn Optimizer"),
    ("GitHub Portfolio", "code", "💻 GitHub Portfolio"),
    ("Executive Report", "assessment", "📑 Executive Report"),
    ("Settings", "settings", "⚙️ Settings"),
    ("HireZeno Enterprise", "corporate_fare", "🏢 HireZeno Enterprise"),
    ("Talent Intelligence", "insights", "💡 Talent Intelligence"),
]


def render_sidebar():
    """
    Render Stitch Light Mode Sidebar Navigation
    Returns:
        str : Selected menu item matching APP_ROUTES keys
    """

    # Check query params for active page
    query_page = st.query_params.get("page", None)
    
    if query_page:
        # Match query param to full key
        for label, icon, full_key in MENU_ITEMS_SPEC:
            if query_page == label or query_page == full_key or urllib.parse.unquote(query_page) == label:
                st.session_state["current_page_key"] = full_key
                break

    if "current_page_key" not in st.session_state:
        st.session_state["current_page_key"] = "📄 Resume Analyzer"

    current_full_key = st.session_state["current_page_key"]

    # Build nav links HTML
    nav_links_html = []
    for label, icon, full_key in MENU_ITEMS_SPEC:
        is_active = (full_key == current_full_key)
        encoded_label = urllib.parse.quote(label)
        
        if is_active:
            link_style = "background-color: #0058bc; color: #ffffff; font-weight: 600; box-shadow: 0 1px 3px rgba(0,0,0,0.1);"
            icon_style = "color: #ffffff;"
        else:
            link_style = "color: #414755; font-weight: 500;"
            icon_style = "color: #414755;"

        html_item = f'<a href="?page={encoded_label}" target="_self" style="text-decoration: none; display: flex; align-items: center; gap: 8px; padding: 8px 12px; border-radius: 8px; font-family: \'Hanken Grotesk\', \'Inter\', sans-serif; font-size: 14px; margin-bottom: 2px; transition: background 0.15s ease; {link_style}"><span class="material-symbols-outlined" style="font-size: 20px; line-height: 1; {icon_style}">{icon}</span><span>{label}</span></a>'
        nav_links_html.append(html_item)

    nav_links_str = "\n".join(nav_links_html)

    # Render entire sidebar HTML cleanly without indentation to prevent markdown code blocks
    sidebar_html = f"""<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
<style>
.stitch-sidebar-header {{
    padding: 4px 8px 12px 8px;
    flex-shrink: 0;
}}
.stitch-sidebar-logo {{
    width: 44px; height: 44px; margin-bottom: 4px;
}}
.stitch-sidebar-title {{
    font-family: 'Hanken Grotesk', sans-serif; font-size: 24px; font-weight: 700; color: #0058bc; margin: 0; line-height: 28px; letter-spacing: -0.01em;
}}
.stitch-sidebar-version {{
    font-family: 'Hanken Grotesk', sans-serif; font-size: 12px; font-weight: 500; color: #414755; opacity: 0.7; margin: 2px 0 0 0;
}}
.stitch-nav-container {{
    flex: 1;
    overflow-y: auto;
    scrollbar-width: none;
    -ms-overflow-style: none;
}}
.stitch-nav-container::-webkit-scrollbar {{
    display: none;
    width: 0;
    height: 0;
}}
.stitch-sidebar-footer {{
    flex-shrink: 0;
    margin-top: auto;
    padding-top: 10px;
}}
.stitch-action-btn {{
    background: linear-gradient(135deg, #005bc1 0%, #4c4aca 100%);
    color: #ffffff !important;
    border: 1px solid rgba(0,0,0,0.05);
    border-radius: 8px;
    padding: 10px 16px;
    font-family: 'Hanken Grotesk', sans-serif;
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(0, 91, 193, 0.15);
    transition: all 0.2s ease;
    width: 100%;
    cursor: pointer;
}}
.stitch-action-btn:hover {{
    background: linear-gradient(135deg, #004493 0%, #3631b4 100%);
    box-shadow: 0 6px 16px rgba(0, 91, 193, 0.25);
}}
</style>

<div style="display: flex; flex-direction: column; height: calc(100vh - 32px); overflow: hidden;">
<div class="stitch-sidebar-header">
<div class="stitch-sidebar-logo">
<img src="{LOGO_URL}" alt="HireZeno Logo" style="width: 100%; height: 100%; object-fit: contain;">
</div>
<h1 class="stitch-sidebar-title">HireZeno 2.0</h1>
<p class="stitch-sidebar-version">{APP_VERSION}</p>
</div>

<nav class="stitch-nav-container">
{nav_links_str}
</nav>

<div class="stitch-sidebar-footer">
<div style="border-top: 1px solid #c1c6d7; padding-top: 12px; margin-bottom: 8px;">
<a href="?action=insights" class="stitch-action-btn" target="_self">
<span class="material-symbols-outlined" style="font-size: 20px; font-variation-settings: 'FILL' 1;">auto_awesome</span>
<span>Generate Insights</span>
</a>
</div>

<div>
<a href="#" style="text-decoration: none; color: #414755; font-family: 'Hanken Grotesk', sans-serif; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 8px; padding: 6px 12px; border-radius: 8px; transition: background 0.2s;" onmouseover="this.style.background='#e4e2e4'" onmouseout="this.style.background='transparent'">
<span class="material-symbols-outlined" style="font-size: 20px; color: #414755;">help_outline</span>
<span>Help Center</span>
</a>
</div>
</div>
</div>"""

    st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

    if st.query_params.get("action") == "insights":
        st.toast("⚡ Generating AI Talent Insights...", icon="✨")

    return current_full_key
