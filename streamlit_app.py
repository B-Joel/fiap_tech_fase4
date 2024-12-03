import streamlit as st
import matplotlib.pyplot as plt

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

st.set_page_config(page_title="PETRÓLEO - BRENT", page_icon=":house:",layout='wide')
st.image(load_img('Imagem/logo.png'))


#Header
with st.container():

    st.title('Bem vindo(a)')
    st.title('Tech Challenge  Fase 4: PETRÓLEO - BRENT')
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    st.write(
        """
        Estudo para a Pós Tech em Data Analytics da FIAP
        
        Grupo 66, Integrantes:
        - rm356228 - Joel Pedro Bellatto
        - rm356366 - Pedro de Almeida Matos
        - rm349836 - Micael Silva Lemos
        - rm355565 - Nathalia Alves da Silva Lima
        """
    )