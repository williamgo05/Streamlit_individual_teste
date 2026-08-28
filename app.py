import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

dados = pd.read_csv(
    "student_lifestyle_100k.csv",
	sep=",",
	encoding="utf-8-sig"
)

dados = dados.drop(["Student_ID","Age","Department"], axis=1)

# print(dados.head())
media = dados.groupby("Depression")["Social_Media_Hours"].mean()
st.subheader("Social Media x Depression")
fig, ax = plt.subplots()
media.plot.bar(ax=ax)
st.pyplot(fig)

sem_depressão = dados[dados["Depression"] == False]
com_depressão = dados[dados["Depression"] == True]

print(sem_depressão["Social_Media_Hours"].median())
print(com_depressão["Social_Media_Hours"].median())

