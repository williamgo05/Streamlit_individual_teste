#Default

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_csv(
    "student_lifestyle_100k.csv",
	sep=",",
	encoding="utf-8-sig"
)

df = df.drop(["Student_ID","Age","Department"], axis=1)

#Default

sem_depressão = df[df["Depression"] == False]
com_depressão = df[df["Depression"] == True]
quantidade = df["Depression"].value_counts()
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

media = df.groupby("Depression")["Social_Media_Hours"].mean()
media.index = ["Sem depressão", "Com depressão"]

with col2:
	st.subheader("Social Media x Depression")
	fig, ax = plt.subplots(figsize=(8, 6))

	fig.patch.set_alpha(0)
	ax.patch.set_alpha(0)

	media.plot.bar(
		ax=ax,
		color=["#1f77b4", "#ff7f0e"]
	)

	ax.tick_params(axis="both", colors="white")
	ax.set_ylabel("Horas", color="white")
	ax.set_title("Média de uso de redes sociais", color="white")

	ax.bar_label(
        ax.containers[0],
        labels=[f"{valor:.2f} h" for valor in media],
        padding=3,
		fontsize=14
		color="white"
    )

	ax.set_title("Média de uso de redes sociais")
	ax.set_ylabel("Horas")
	ax.tick_params(axis="x", labelrotation=0)
	ax.set_ylim(0, 4)

	ax.plot(
		[0, 1],
		[media.iloc[0], media.iloc[0]],
		linestyle="--",
		color="#1f77b4"
	)

	st.pyplot(fig)
