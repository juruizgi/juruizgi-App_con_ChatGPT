# Importar la biblioteca Streamlit
import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.text("Esta app fue elaborada por Juan David Ruiz Giraldo")

# Preguntar el nombre al usuario mediante un cuadro de texto
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Verificar si se ingresó un nombre
if nombre_usuario:
    # Mostrar el mensaje de bienvenida con el nombre del usuario
    mensaje_bienvenida = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje_bienvenida)
