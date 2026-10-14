import streamlit as st

st.title("Hola, Mundo 👋")
st.subheader("Este es el primero módulo que desarrollo en la semana 1 del curso")

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"¡Hola, {nombre}! Esta es mi primera app en internet.")

st.info(f"✳ - Versión 0. Módulo Fundamentos de Programación")
