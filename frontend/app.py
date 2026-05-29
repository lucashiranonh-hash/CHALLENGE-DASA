import streamlit as st

st.title("Assistente Genético Genera")

pergunta = st.text_input("Faça sua pergunta")

if pergunta:
    st.write("Resposta simulada baseada no relatório.")
