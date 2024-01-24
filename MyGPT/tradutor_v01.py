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

st.title("Tradutor de Textos para inglês")
st.write('***')

st.subheader("Texto em português")
texto_original = st.text_area("Escreva seu texto em português: ")

if texto_original:
    texto_traduzido = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role":"user", "content":"Traduza o texto a seguir para o idioma inglês: " + texto_original}]
    )
    st.write("***")
    st.subheader("Tradução: ")
    st.write(texto_traduzido.choices[0].message.content)