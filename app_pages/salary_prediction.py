import streamlit as st


def salary_prediction_page():
    """
    Salary Prediction Page
    """

    st.header("💼 Salary Prediction")

    exp = st.slider(
        "Experience (Years)",
        0,
        20,
        2
    )

    estimated_salary = 5 + (exp * 2)

    st.metric(
        "Estimated Salary",
        f"₹ {estimated_salary} LPA"
    )

    st.info(
        "This is a demo salary estimator. Future versions will use ML models."
    )
