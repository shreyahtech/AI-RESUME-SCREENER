import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


# ---------------------- Gauge ----------------------

def show_gauge(score):

    if score >= 75:
        color = "#00cc66"
    elif score >= 50:
        color = "#ffcc00"
    else:
        color = "#ff4d4d"


    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={
                "suffix": "%",
                "font": {"size": 40}
            },
            title={
                "text": "Overall Match Score",
                "font": {"size": 22}
            },
            gauge={
                "axis": {
                    "range": [0,100]
                },

                "bar": {
                    "color": color
                },

                "steps":[
                    {
                        "range":[0,50],
                        "color":"rgba(255,0,0,0.15)"
                    },
                    {
                        "range":[50,75],
                        "color":"rgba(255,200,0,0.15)"
                    },
                    {
                        "range":[75,100],
                        "color":"rgba(0,255,100,0.15)"
                    }
                ]
            }
        )
    )


    fig.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ---------------------- Candidate Comparison ----------------------

def show_candidate_bar(df):

    df = df.sort_values(
        by="Score",
        ascending=False
    )


    fig = px.bar(
        df,
        x="Candidate",
        y="Score",
        text="Score",
        title="Candidate Ranking",
        color="Score",
        color_continuous_scale="Blues"
    )


    fig.update_traces(
        textposition="outside"
    )


    fig.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ---------------------- Skill Match ----------------------

def show_skill_pie(matched, missing):


    fig = px.pie(
        values=[
            matched,
            missing
        ],

        names=[
            "Matched Skills",
            "Missing Skills"
        ],

        hole=0.55,

        title="Skill Match Analysis",

        color_discrete_sequence=[
            "#00cc99",
            "#ff6666"
        ]
    )


    fig.update_traces(
        textinfo="percent+label"
    )


    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )