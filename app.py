import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Mi App Streamlit",
    page_icon="🚀",
    layout="wide"
)

# Título principal
st.title("🚀 Mi Primera App Streamlit en Docker")
st.markdown("---")

# Sidebar
st.sidebar.header("Configuración")
nombre = st.sidebar.text_input("Tu nombre:", "Usuario")
edad = st.sidebar.slider("Tu edad:", 1, 100, 25)
# --- CÓDIGO AGREGADO PARA IMC ---
peso = st.sidebar.number_input("Tu peso (kg):", min_value=10.0, max_value=200.0, value=70.0, step=0.1)
estatura = st.sidebar.slider("Tu estatura (metros):", min_value=1.0, max_value=2.5, value=1.70, step=0.01)
imc = peso / (estatura ** 2)
# --------------------------------

# Contenido principal
col1, col2 = st.columns(2)

with col1:
    st.header(f"¡Hola {nombre}!")
    st.write(f"Tienes {edad} años")
    
    # Botón interactivo
    if st.button("Generar datos aleatorios"):
        st.success("¡Datos generados exitosamente!")

with col2:
    st.header("📊 Gráfico de ejemplo")
    
    # Generar datos aleatorios
    data = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10).cumsum(),
        'categoria': np.random.choice(['A', 'B', 'C'], 10)
    })
    
    # Crear gráfico
    fig = px.line(data, x='x', y='y', color='categoria', 
                  title="Datos Aleatorios")
    st.plotly_chart(fig, use_container_width=True)

# Métricas
st.markdown("---")
st.header("📈 Métricas")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Usuarios", "1,234", "12%")
with col2:
    st.metric("Ventas", "$5,678", "-2%")
with col3:
    st.metric("Conversión", "3.4%", "0.5%")
# --- MODIFICADO PARA MOSTRAR IMC ---
with col4:
    st.metric("Tu IMC", f"{imc:.1f}")
    if imc < 18.5:
        st.info("Bajo peso")
    elif 18.5 <= imc < 25:
        st.success("Peso normal")
    elif 25 <= imc < 30:
        st.warning("Sobrepeso")
    else:
        st.error("Obesidad")
# -----------------------------------

# Tabla de datos
st.markdown("---")
st.header("📋 Tabla de Datos")
st.dataframe(data, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Aplicación creada con Streamlit y Docker** 🐳")

