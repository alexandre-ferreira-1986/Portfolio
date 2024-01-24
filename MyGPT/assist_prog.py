from openai import OpenAI
import streamlit as st
import sys
import json
import os
from dotenv import load_dotenv

# Carregar ENV
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

st.title("Assistente de programação")
st.write("***")

st.subheader("Pergunta")
pergunta = st.text_area("Digite sua pergunta no quadro: ")

st.sidebar.header("Configurações")
st.sidebar.write("***")
form_config = st.sidebar.form("config_form")
form_config.subheader("Selecione o tipo de resposta")
tipo_resposta = form_config.radio("Tipo de Resposta", ("Texto", "Código"))
linguagem = form_config.selectbox("Selecione a linguagem de programação", ("Python", "Linguagem R", "Java", "Javascript", "HTML", "CSS", "React"))
submeter = form_config.form_submit_button("OK")

st.subheader("Resposta")
if submeter:
    if tipo_resposta == "Texto":
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role":"user", "content":pergunta}]
        )
    
        st.write(resposta.choices[0].message.content)

    else: 
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role":"user", "content":pergunta + f". O código deve ser em {linguagem}"}]
        )
        st.code(resposta.choices[0].message.content, language=linguagem.lower())

