import streamlit as st
import time


# Ícone no topo (favicon)
st.set_page_config(
    page_title="ChatBot IA - by Markos",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS com avatares
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
        }
        .stApp {
            background: linear-gradient(160deg, #0f0f0f 0%, #1a1a1a 100%);
        }
        .chat-message {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin: 10px 0;
        }
        .chat-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }
        .chat-bubble {
            background-color: #262730;
            color: white;
            padding: 10px 15px;
            border-radius: 12px;
            max-width: 80%;
            line-height: 1.5;
        }
        .user-bubble {
            background-color: #1f1f1f;
            color: #00ffff;
        }
        .title-center {
            text-align: center;
            color: #00ffff;
            font-size: 50px;
            margin-bottom: 30px;
        }
        .intro-text {
            text-align: center;
            font-size: 20px;
            color: #cccccc;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Título com emoji e centralizado
st.markdown('<div class="title-center">🤖 ChatBot com IA - by Markos </div>', unsafe_allow_html=True)

# Estado inicial
if "inicio" not in st.session_state:
    st.session_state.inicio = True 
    st.markdown('<div class="intro-text">Primeiramente, tudo bem? Aqui é o Markos. Esse é um teste com IA estilo ChatGPT. Manda tua mensagem aí! 😉</div>', unsafe_allow_html=True)
else:
    st.markdown("---")

# Entrada do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui jovem:")

# Lista de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Função para exibir mensagens com avatar
def exibir_mensagem(role, content):
    avatar_url = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png" if role == "assistant" else "https://img.icons8.com/?size=100&id=77180&format=png&color=000000"
    bubble_class = "chat-bubble" if role == "assistant" else "chat-bubble user-bubble"
    
    st.markdown(f"""
        <div class="chat-message">
            <img src="{avatar_url}" class="chat-avatar" />
            <div class="{bubble_class}">{content}</div>
        </div>
    """, unsafe_allow_html=True)

# Exibir histórico
for mensagem in st.session_state["lista_mensagens"]:
    exibir_mensagem(mensagem["role"], mensagem["content"])

# Processar nova mensagem
if mensagem_usuario:
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})
    exibir_mensagem("user", mensagem_usuario)

    time.sleep(1)

    msg = mensagem_usuario.lower()
    if "iai" in msg:
        resposta = "iai, belezinha!"
    elif "oi" in msg:
        resposta = "oi, que bom que veio testar!"
    elif "legal" in msg:
        resposta = "então, achei da hora tambem, bem interresante!"
    elif "gay" in msg:
        resposta = "gay é tu kkkk"
    elif "viado" in msg:
        resposta = "não tenho tuas manias kkk"
    elif "corno" in msg:
        resposta = "eu ?, to vendo teu chifre daqui kkkk"
    elif "boi" in msg:
        resposta = "iai lambe sal kkk"
    elif "baitola" in msg:
        resposta = "tu quer dar tu fala kkk"
    elif "qualira" in msg:
        resposta = "vira de costa ai kkk"
    elif "fresco" in msg:
        resposta = "o que tu quer ta é duro kkkk"
    elif "chifrudo" in msg:
        resposta = "tu anda com cabide na cabeça, ou é outra parada ? kkkk"
    elif "solteiro" in msg:
        resposta = "faz tempo que não, tenho minha gatinha ja, so alegria!!"
    elif "casado" in msg:
        resposta = "ainda não, mas eu vou, fique de boa"
    elif "casar" in msg:
        resposta = "vou, com certeza!!"
    elif "me ama" in msg or "você me ama" in msg:
        resposta = "Mais do que tudo nesse mundo! 🥰"
    elif "sente minha falta" in msg:
        resposta = "Morro de saudade toda hora que você some! 😢❤️"
    elif "tá com outra" in msg:
        resposta = "Com outra? Só se for outra versão de você no espelho! 😅"
    elif "bravo comigo" in msg:
        resposta = "Nunca fico bravo de verdade... só com saudade. 💕"
    elif "tá me ignorando" in msg:
        resposta = "Jamais! Eu tô aqui só pensando em você. 💌"
    elif "me acha linda" in msg:
        resposta = "Você é a definição de perfeição, meu amor! 😍"
    elif "vai me largar" in msg:
        resposta = "Só se for pra te agarrar mais forte depois. 😘"
    else:
        resposta = "Você quis dizer: " + mensagem_usuario

    st.chat_message("assistant").write(resposta)
    mensagem_ia = {"role": "assistant", "content": resposta}
    st.session_state["lista_mensagens"].append(mensagem_ia)
