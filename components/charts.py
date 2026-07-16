import plotly.graph_objects as go
import streamlit as st


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