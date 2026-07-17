import streamlit as st


def show_summary(df):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Match",
            f"{df['Score'].mean():.1f}%"
        )

    with col2:
        st.metric(
            "Highest Match",
            f"{df['Score'].max():.1f}%"
        )

    with col3:
        st.metric(
            "Lowest Match",
            f"{df['Score'].min():.1f}%"
        )

    with col4:
        st.metric(
            "Average ATS",
            f"{df['ATS Score'].mean():.1f}%"
        )