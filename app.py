import streamlit as st
import json 
import pandas as pd

st.markdown ("# Saúde do Sono e Estilo de Vida")

st.markdown('## Dados')
df = pd.read_csv('dataset.csv')
st.write(df)
