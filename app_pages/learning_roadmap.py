import streamlit as st
from core.learning_recommender import LearningRecommender


def learning_roadmap_page():
    """
    Learning Roadmap Page
    """

    st.header("📚 AI Learning Roadmap")

    lr = LearningRecommender()

    st.subheader("Recommended Learning Path")

    st.dataframe(
        lr.learning,
        use_container_width=True
    )

    st.success(
        "Learning roadmap loaded successfully."
    )
