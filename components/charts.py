import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


# ---------------------- Gauge ----------------------

def show_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Overall Match Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "royalblue"},
                "steps": [
                    {"range": [0, 50], "color": "#ffcccc"},
                    {"range": [50, 75], "color": "#ffe699"},
                    {"range": [75, 100], "color": "#ccffcc"},
                ],
            },
        )
    )

    fig.update_layout(height=350)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------- Candidate Comparison ----------------------

def show_candidate_bar(df):

    fig = px.bar(
        df,
        x="Candidate",
        y="Score",
        color="Score",
        text="Score",
        title="Candidate Match Scores"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        height=450,
        xaxis_title="Candidate",
        yaxis_title="Match Score"
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------------- Skill Match ----------------------

def show_skill_pie(matched, missing):

    fig = px.pie(
        values=[matched, missing],
        names=["Matched Skills", "Missing Skills"],
        hole=0.5,
        title="Skill Match Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)