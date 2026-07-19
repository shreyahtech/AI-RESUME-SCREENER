import streamlit as st


def show_candidate_list(df):

    st.subheader("🏆 Candidate Rankings")

    for _, row in df.iterrows():

        st.markdown(
            f"""
            <div class="candidate-row">

                <div>
                    <h3>👤 {row["Candidate"]}</h3>

                    <p>
                        🎯 ATS Score: {row["ATS Score"]}%
                    </p>
                </div>

                <div class="rank-score">

                    ⭐ {row["Score"]}%

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )