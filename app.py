import streamlit as st
from faker import Faker
import pandas as pd
import numpy as np

fake = Faker('es_ES')

available_fields = {
    "Nombre": fake.name,
    "Dirección": fake.address,
    "Email": fake.email,
    "Teléfono": fake.phone_number,
    "Fecha de nacimiento": fake.date_of_birth,
    "Número de tarjeta de crédito": fake.credit_card_number,
    "Empresa": fake.company,
    "Cargo": fake.job
}

def generate_data(num_rows, fields):
    data = {col: [available_fields[col]() for _ in range(num_rows)] for col in fields}
    return pd.DataFrame(data)

st.title("Generador de Datos Falsos con Faker.")
st.write("Selecciona los atributos a generar y la cantidad de instancias.")

selected_fields = st.multiselect("Selecciona los atributos a generar:", 
                                 options=list(available_fields.keys()), 
                                 default=list(available_fields.keys()))

num_rows = st.number_input("Cantidad de instancias", 
                           min_value=1, max_value=1000, value=10, step=1)

if st.button("Generar Datos"):
    if selected_fields:
        data = generate_data(num_rows, selected_fields)
        st.success("Datos generados con éxito.")
        st.write(data)
        st.download_button("Descargar CSV", data.to_csv(index=False), "datos_falsos.csv", "text/csv")
    else:
        st.warning("Por favor, selecciona al menos un atributo.")
        st.info("Puedes seleccionar múltiples atributos para generar datos falsos.")

