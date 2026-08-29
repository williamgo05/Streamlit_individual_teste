import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

dados = pd.read_csv(
    "student_lifestyle_100k.csv",
	sep=",",
	encoding="utf-8-sig"
)

dados = dados.drop(["Student_ID","Age","Department"], axis=1)

sem_depressão = dados[dados["Depression"] == False]
com_depressão = dados[dados["Depression"] == True]
quantidade = dados["Depression"].value_counts()
quantidade.index = ["Sem depressão", "Com depressão"]

col1, col2 = st.columns(2)

with col1:
	st.subheader("Distribuição de estudantes por depressão")
	fig, ax = plt.subplots(figsize=(8, 6))
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
	fig, ax = plt.subplots(figsize=(8, 6))
	media.plot.bar(ax=ax)
	ax.set_title("Média de uso de redes sociais")
	ax.set_ylabel("Horas")

	st.pyplot(fig)
