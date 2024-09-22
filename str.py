import streamlit as st
import os
import subprocess

# Função para instalar pacotes
def install_packages():
    try:
        subprocess.check_call(["pip", "install", "yt-dlp", "--upgrade"])
        subprocess.check_call(["pip", "install", "--index-url", "https://test.pypi.org/simple/", "extrator_audio"])
    except Exception as e:
        st.error(f"Erro ao instalar pacotes: {e}")

# Instala as bibliotecas
install_packages()

# Importa a função após a instalação
from extrator_audio.doau import extrair_audio

# Interface do Streamlit
st.title("Extrator de Áudio do YouTube")

# Campo para o usuário colar o link do vídeo
url = st.text_input("Cole o link do vídeo do YouTube:")

# Campo para o caminho de saída
caminho_saida = st.text_input("Caminho da pasta de destino (ex: C:/Users/SeuUsuario/Pasta):")

# Botão de download
if st.button("Extrair Áudio"):
    if url and caminho_saida:
        if not os.path.exists(caminho_saida):
            st.error("O caminho de saída não existe. Por favor, verifique.")
        else:
            resultado = extrair_audio(url, caminho_saida=caminho_saida)
            st.success(f"Áudio salvo em: {resultado}")
    else:
        st.error("Por favor, preencha todos os campos.")
