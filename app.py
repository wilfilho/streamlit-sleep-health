import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown ("# Saúde do Sono e Estilo de Vida")

st.markdown('## Dados')
data = pd.read_csv('dataset.csv')

st.header("Correlação: Distúrbios do Sono, Duração do Sono e Ocupação")
plt.figure(figsize=(12, 6))
sns.boxplot(x='Occupation', y='SleepDuration', hue='SleepDisorder', data=data)
plt.title("Duração do Sono por Ocupação e Presença de Distúrbios do Sono")
plt.xlabel("Ocupação")
plt.ylabel("Duração do Sono (horas)")
plt.xticks(rotation=45)
st.pyplot(plt)

st.header("Atividade Física vs. Duração do Sono")
plt.figure(figsize=(10, 5))
plt.scatter(data['PhysicalActivity'], data['SleepDuration'], alpha=0.6)
plt.title("Atividade Física vs Sono")
plt.xlabel("Nível de Atividade Física")
plt.ylabel("Horas de Sono")
st.pyplot(plt)

st.write(data)

# st.header("Distribuição das Horas de Sono")
# plt.figure(figsize=(10, 5))
# plt.hist(data['SleepDuration'], bins=20, alpha=0.7, edgecolor='black')
# plt.title("Distribuição de Duração do Sono")
# plt.xlabel("Horas de Sono")
# plt.ylabel("Frequência")
# st.pyplot(plt)
