# titulo
# input do chat
# a cada mensagem enviada:
# mostrar a mensagem que o usuario enviou no chat
# enviar essa mensagem para a IA responder
# aparece na tela a resposta da IA

# streamlit - frontend e backend

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="") #link do seu API(necessita de MONEY)

st.write("### Bem vindo ao Chat_Kael")  # markdown

# session_state = memória do streamlit
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []


# adicionar uma mensagem
# session_state = ["lista_mensagens"].append(mensagem)

#exibir o historico 
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    texto = mensagem["content"]
    st.chat_message("role").write(texto)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:

    # user -> ser humano

    # assistent -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # rsposta IA  #Openeai api
    reposta_modelo = modelo.chat.completions.create(
        mensagem = st.session_state["lista_mensagens"],
        model="" #versão do Openai
    )
    print(reposta_modelo)
    resposta_ia = reposta_modelo.choices[0].message.content
    resposta_ia = "você quis dizer: " + mensagem_usuario    

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistent", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

    print(st.session_state["lista_mensagens"])