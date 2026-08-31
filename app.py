#Default

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

dados = pd.read_csv(
    "student_lifestyle_100k.csv",
	sep=",",
	encoding="utf-8-sig"
)

dados = dados.drop(["Student_ID","Age","Department"], axis=1)

#Default

sem_depressão = dados[dados["Depression"] == False]
com_depressão = dados[dados["Depression"] == True]
quantidade = dados["Depression"].value_counts()
quantidade.index = ["Sem depressão", "Com depressão"]

col1, col2 = st.columns(2)

with col1:
	st.subheader("Distribuição de estudantes por depressão")
	fig, ax = plt.subplots(figsize=(10, 7))
	total = quantidade.sum()

	ax.pie(
		quantidade,
		labels=quantidade.index,
		autopct=lambda pct: f"{pct:.1f}%\n({int(pct * total / 100):,})"
	)

	st.pyplot(fig)

media = dados.groupby("Depression")["Social_Media_Hours"].mean()
media.index = ["Sem depressão", "Com depressão"]

with col2:
	st.subheader("Social Media x Depression")
	fig, ax = plt.subplots(figsize=(10, 7))
	media.plot.bar(ax=ax)
	ax.bar_label(
        ax.containers[0],
        labels=[f"{valor:.2f} h" for valor in media],
        padding=3
    )

	ax.set_title("Média de uso de redes sociais")
	ax.set_ylabel("Horas")
	ax.tick_params(axis="x", labelrotation=0)

	st.pyplot(fig)
