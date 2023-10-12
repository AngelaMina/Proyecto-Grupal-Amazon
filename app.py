# %%writefile app.py 

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="AGEC Data Consulting", page_icon="🤖", layout="wide")

# fución para nuestra animación
def load_lottieurl(url):
    r = requests.get (url)
    if r.status_code != 200:
        return None
    return r.json()

# fución para datos

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="emailcontact@gmail.com"

#  variables

lottie_coding = load_lottieurl("https://lottie.host/d7fa2755-5843-47b9-b185-e666b47ed7ca/0CRGQXx2WO.json")
imagen_logo = Image.open("imagenes/Logo.PNG")
lottie_figureone = load_lottieurl("https://lottie.host/b4ed557d-cf42-455b-848f-5ff480e070e8/drOD2LHJWF.json") 
lottie_figuretwo = load_lottieurl("https://lottie.host/2a42fc01-a2c1-4f0a-8bc2-c18a86b656ad/tDhOCvUAeQ.json")
imagen_azure = Image.open("imagenes/entorno.PNG")
imagen_power = Image.open("imagenes/power_bi.PNG")
imagen_streamlit = Image.open("imagenes/streamlit.PNG")
imagen_angela = Image.open("imagenes/Angela.PNG")
imagen_cristhian = Image.open("imagenes/Cristhian.PNG")
imagen_esteban = Image.open("imagenes/Esteban.PNG")
imagen_gaston =Image.open("imagenes/Gaston.PNG")

# 1 contenedor

with st.container():
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>AGEC DATA CONSULTING</h1>", unsafe_allow_html=True)

# 2 contenedor

with st.container():
    st.write("---")
    st. header("NUESTRA MISIÓN")
    image_column, text_column = st.columns ((2, 1))
    with image_column:
        st.image(imagen_logo)
    with text_column:
        st.write(
          """Fusionar la analítica de ventas y reseñas con la inteligencia artificial, creando herramientas tecnológicas que ayuden a mejorar la experiencia del cliente y aumentar las ventas.""")
        st.write("[Mas información >](https://github.com/AngelaMina/Proyecto-Grupal-Amazon)")

# 3 contenedor

with st.container():
    st.write("---")

    # Dividir el contenedor en dos columnas
    columna_izquierda, columna_derecha = st.columns(2)

    # Contenido para la columna izquierda
    with columna_izquierda:
      st.header("NUESTROS CLIENTES")
      st.write(
          """Amazon, un líder indiscutible en innovación y satisfacción del cliente, busca mantener su posición destacada en el mercado estadounidense al colaborar con nuestra consultora."""
          )
      st.header("Beneficios")
      st.write("🎯 Diseño y construcción de arquitectura de datos eficiente y escalable")
      st.write("🎯 Modelo de recomendación")
      st.write("🎯 Interfaz de usuario funcional")
      st.write("🎯 Documentación del Proyecto")

    # Contenido para la columna derecha
    with columna_derecha:
      st_lottie(lottie_coding, height=300, key="coding")

# 4 contenedor

with st.container():
    st.write("---")

    st.header("CÓMO FUNCIONA")

    # Dividir el contenedor en dos columnas
    columna_izquierda, columna_derecha = st.columns(2)

    # Contenido para la columna izquierda
    with columna_izquierda:
      st_lottie(lottie_figureone, height=400, key="coding1")

    # Contenido para la columna derecha
    with columna_derecha:
      st.header("/01 Análisis de datos")
      st.write(
      """El análisis de datos es esencial para nuestra plataforma, ya que nos permite recopilar, analizar y comprender información valiosa sobre los negocios. Esta información respalda decisiones informadas que pueden impulsar mejoras en el éxito de los negocios. Utilizamos el análisis de datos para comprender el comportamiento de los clientes, identificar oportunidades de crecimiento y optimizar la eficiencia, lo que, a su vez, puede aumentar las ventas, mejorar el servicio al cliente y reducir los costos.
      """
      )
      st.write("[Ver Dashboard >](https://www.youtube.com/watch?v=zeS2FlxF_0s&ab_channel=Dr.Xabi)")

# 5 contenedor

with st.container():
    st.write("---")

    # Dividir el contenedor en dos columnas
    columna_izquierda, columna_derecha = st.columns(2)

    # Contenido para la columna izquierda
    with columna_izquierda:
      st.header("/02 Machine Learning")
      st.write(
        """ Los sistemas de recomendación de AGEC Data Consulting, utilizan machine learning para crear recomendaciones personalizadas para cada usuario. El machine learning nos permite aprender de los datos de Amazon para identificar patrones y tendencias que pueden ayudar al negocio a mejorar su éxito.
            Estos sistemas pueden ayudarte a aumentar las ventas, mejorar la satisfacción del cliente.
        """
        )

    # Contenido para la columna derecha
    with columna_derecha:
      st_lottie(lottie_figuretwo, height=400, key="coding2")

# 6 contenedor

with st.container():
    st.write("---")

    st.header("SISTEMA DE RECOMEDACIÓN")
# 7 contenedor

with st.container():
    st.write("---")

    st.header("TECNOLOGÍAS USADAS")

    # Divide el contenedor en 3 columnas para las imágenes
    col1, col2, col3 = st.columns(3)

    # Muestra las imágenes en cada columna
    with col1:
        st.image(imagen_azure, width=175)

    with col2:
        st.image(imagen_power, width=125)

    with col3:
        st.image(imagen_streamlit, width=150)

# 8 contenedor

with st.container():
    st.write("---")

    st.header("NOSOTROS")

    # Divide el contenedor en 4 columnas para las imágenes
    col1, col2, col3, col4 = st.columns(4)

    # Muestra las imágenes en cada columna
    with col1:
        st.image(imagen_angela, width=100)
        st.write("Data Scientist")

    with col2:
        st.image(imagen_cristhian, width=100)
        st.write("Data Scientist")

    with col3:
        st.image(imagen_esteban, width=100)
        st.write("Data Scientist")

    with col4:
        st.image(imagen_gaston, width=100)
        st.write("Data Scientist")
        
# 9 contenedor

with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

