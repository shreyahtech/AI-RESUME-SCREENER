import pandas as pd
import streamlit as st


def show_comparison(df):

    st.subheader("📊 Candidate Comparison")

    comparison = pd.DataFrame(
        {
            "Candidate": df["Candidate"],
            "Match Score": df["Score"],
            "ATS Score": df["ATS Score"],
            "Skills": df["Skill List"].apply(len),
            "Missing Skills": df["Missing Skill List"].apply(len),
            "LinkedIn": df["Details"].apply(
                lambda x: "✅" if x["linkedin"] != "Not Found" else "❌"
            ),
            "GitHub": df["Details"].apply(
                lambda x: "✅" if x["github"] != "Not Found" else "❌"
            ),
        }
    )

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )