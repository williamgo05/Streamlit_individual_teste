# Default

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv(
    "student_lifestyle_100k.csv",
    sep=",",
    encoding="utf-8-sig"
)

df = df.drop(["Student_ID", "Age", "Department"], axis=1)

# Default

quantidade = df["Depression"].value_counts()
quantidade.index = ["Sem depressão", "Com depressão"]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição de estudantes por depressão")

    fig = px.pie(
        values=quantidade,
        names=quantidade.index,
        color=quantidade.index,
        color_discrete_sequence=["#1f77b4", "#ff7f0e"]
    )

    fig.update_traces(
        texttemplate="%{label}<br>%{percent:.1%}<br>(%{value:,})",
        textfont=dict(color="white"),
        textposition="outside",
        showlegend=False
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)


media = df.groupby("Depression")["Social_Media_Hours"].mean()
media.index = ["Sem depressão", "Com depressão"]

with col2:
    st.subheader("Social Media x Depression")

    fig = px.bar(
        x=media.index,
        y=media.values,
        color=media.index,
        color_discrete_sequence=["#1f77b4", "#ff7f0e"],
        text=[f"{valor:.2f} h" for valor in media]
    )

    fig.update_traces(
        textposition="outside",
        textfont=dict(color="white"),
        width=0.55
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title=dict(
            text="Média de uso de redes sociais",
            x=0.5
        ),
        yaxis_title="Horas",
        xaxis_title="",
        showlegend=False,
        yaxis_range=[0, 4]
    )

    fig.add_hline(
        y=media.iloc[0],
        line_dash="dash",
        line_color="#1f77b4"
    )

    st.plotly_chart(fig, use_container_width=True)