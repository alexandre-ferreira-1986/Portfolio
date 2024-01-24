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

st.title("Meu primeiro App")

pergunta = st.text_input("Escreva aqui sua mensagem: ")

if pergunta:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role":"user", "content":pergunta}]
    )

    st.subheader("RESPOSTA")
    st.write(response.choices[0].message.content)

    
        


