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

# Inicializa ou recupera o estado da sessão
if 'list_messages' not in st.session_state:
    st.session_state.list_messages = []

st.subheader("Resposta")

if submeter:

    # Adiciona a pergunta ao histórico da sessão
    mensagem_usuario = {"role": "user", "content": pergunta}
    st.session_state.list_messages.append(mensagem_usuario)
    
    # Escolha entre texto e código
    if tipo_resposta == "Código":
        mensagem_usuario["content"] += f". O código deve ser em {linguagem}"
    
    try:
        # Realiza a chamada à API
        resposta = client.chat.completions.create(
            model='gpt-3.5-turbo-1106',
            messages=st.session_state.list_messages
        )
        
        # Exibe a resposta e atualiza a sessão
        resposta_texto = resposta.choices[0].message.content
        st.session_state.list_messages.append({"role": "system", "content": resposta_texto})
        if tipo_resposta == "Texto":
            st.write(resposta_texto)
        else:
            st.code(resposta_texto, language=linguagem.lower())
    except Exception as e:
        st.error(f"Erro ao obter resposta: {e}")

