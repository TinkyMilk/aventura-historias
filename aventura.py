import streamlit as st

st.title("🧙‍♂️ Creador de Historias Fantásticas")

nombre = st.text_input("¿Cuál es tu nombre?")
animal = st.text_input("¿Cuál es tu animal favorito?")
lugar = st.text_input("Nombra un lugar mágico")
accion = st.text_input("¿Qué acción hace tu animal? (ej: volar, cantar)")

if st.button("✨ Crear historia"):
    if nombre and animal and lugar and accion:
        historia = f"""
        Había una vez una aventurera llamada {nombre},  
        que un día encontró un {animal} en {lugar}.  
        Este {animal} tenía un poder mágico: podía {accion}.  
        Desde entonces, {nombre} y su amigo vivieron increíbles aventuras.
        """
        st.success(historia)
    else:
        st.warning("Por favor, completa todos los campos para crear tu historia.")
