from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interface Streamlit
st.title("Personal Assistant")
st.subheader("Question")
pergunta = st.text_area("Type your question: ", key="pergunta")

# Configurações na barra lateral
st.sidebar.header("Settings")
form_config = st.sidebar.form("config_form")
tipo_resposta = form_config.radio("Type of Answer", ("Text", "Code"))
linguagem = form_config.selectbox("Select Programming Language", ("Python", "Linguagem R", "Java", "Javascript", "HTML", "CSS", "React"))
submeter = form_config.form_submit_button("OK")

gpt_config = st.sidebar.form("gpt_config")
gpt_config.subheader("Model Type")
modelo_gpt = gpt_config.radio("Model",('3.5', '4.0'))
modelo_aplicado = "gpt-3.5-turbo-1106"
if modelo_gpt == '3.5':
    modelo_aplicado = "gpt-3.5-turbo-1106"
else:
    modelo_aplicado = "gpt-4-1106-preview"
submete_modelo = gpt_config.form_submit_button("Modelo")

# Inicializa ou recupera o estado da sessão
if 'list_messages' not in st.session_state:
    st.session_state.list_messages = []

if (submeter or submete_modelo) and pergunta:
    # Adiciona a pergunta ao histórico da sessão
    st.session_state.list_messages.append({"role": "user", "content": pergunta})
    
    # Escolha entre texto e código
    if tipo_resposta == "Code":
        st.session_state.list_messages[-1]["content"] += f". O código deve ser em {linguagem}"

    try:
        # Realiza a chamada à API
        resposta = client.chat.completions.create(
            model=modelo_aplicado,
            messages=st.session_state.list_messages
        )
        
        # Exibe a resposta e atualiza a sessão
        resposta_texto = resposta.choices[0].message.content
        st.session_state.list_messages.append({"role": "system", "content": resposta_texto})

    except Exception as e:
        st.error(f"Erro ao obter resposta: {e}")

# Exibir histórico de mensagens
st.subheader("Messages")
for mensagem in st.session_state.list_messages:
    role = mensagem["role"]
    content = mensagem["content"]
    if role == "user":
        # Aplicando um estilo CSS para destacar as perguntas do usuário
        st.markdown(f"<div style='background-color: #e8f4fa; padding: 10px; border-radius: 5px;; color: black;'>**Você:** {content}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"**Assistente:** {content}")
