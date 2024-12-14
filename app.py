import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown ("# Saúde do Sono e Estilo de Vida")

st.markdown('## Dados')
data = pd.read_csv('dataset.csv')
st.write(data)

st.header("Distribuição das Horas de Sono")
plt.figure(figsize=(10, 5))
plt.hist(data['Sleep_Duration'], bins=20, alpha=0.7, edgecolor='black')
plt.title("Distribuição de Duração do Sono")
plt.xlabel("Horas de Sono")
plt.ylabel("Frequência")
st.pyplot(plt)
