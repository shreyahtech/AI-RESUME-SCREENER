import streamlit as st


def show_top_candidates(df):

    st.subheader("🥇 Top Candidates")

    medals = ["🥇", "🥈", "🥉"]

    top = df.head(3)

    for i, (_, row) in enumerate(top.iterrows()):

        st.info(
            f"{medals[i]}  {row['Candidate']}  |  Match: {row['Score']}%  |  ATS: {row['ATS Score']}%"
        )