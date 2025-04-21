import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Madrid Seguro 2024", layout="wide")

st.title("🚦 Dashboard de Atropellos en Madrid - 2024")
st.markdown("Visualización de la gravedad de los atropellos en los distritos de Madrid según datos de 2024.")

# Datos de ejemplo
data = pd.DataFrame({
    "Distrito": ["Chamartín", "Centro", "Salamanca", "Retiro", "Usera", "Tetuán"],
    "Lesiones Graves (%)": [35, 22, 18, 11, 8, 6]
})

fig = px.bar(data, x="Distrito", y="Lesiones Graves (%)", color="Distrito", text="Lesiones Graves (%)")
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title="Porcentaje de Lesiones Graves por Distrito en 2024", yaxis_range=[0, 40])

st.plotly_chart(fig, use_container_width=True)

