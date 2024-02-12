import streamlit as st

def convertir_temperatura(valor, desde, hacia):
    if desde == "Celsius" and hacia == "Fahrenheit":
        return (valor * 9/5) + 32
    elif desde == "Fahrenheit" and hacia == "Celsius":
        return (valor - 32) * 5/9
    elif desde == "Celsius" and hacia == "Kelvin":
        return valor + 273.15
    elif desde == "Kelvin" and hacia == "Celsius":
        return valor - 273.15
    else:
        return valor  # Si las unidades son las mismas, no hay conversión

def convertir_longitud(valor, desde, hacia):
    # Definir las conversiones de longitud
    conversiones = {
        ("Pies", "Metros"): valor * 0.3048,
        ("Metros", "Pies"): valor / 0.3048,
        ("Pulgadas", "Centímetros"): valor * 2.54,
        ("Centímetros", "Pulgadas"): valor / 2.54
    }
    return conversiones.get((desde, hacia), valor)

# Definir las demás funciones de conversión para las categorías restantes...

def main():
    st.title("Conversor Universal")

    # Seleccionar la categoría de conversión
    categoria = st.selectbox("Selecciona una categoría:", ["Temperatura", "Longitud"])

    # Seleccionar las unidades de conversión dentro de la categoría seleccionada
    if categoria == "Temperatura":
        unidades = st.multiselect("Selecciona las unidades:", ["Celsius", "Fahrenheit", "Kelvin"])
    elif categoria == "Longitud":
        unidades = st.multiselect("Selecciona las unidades:", ["Pies", "Metros", "Pulgadas", "Centímetros"])
    # Agregar las demás categorías...

    # Ingresar el valor a convertir
    valor = st.number_input("Ingresa el valor a convertir:", value=0.0)

    # Realizar la conversión
    if st.button("Convertir"):
        resultado = valor  # Valor predeterminado si no hay conversión

        if categoria == "Temperatura" and len(unidades) == 2:
            resultado = convertir_temperatura(valor, unidades[0], unidades[1])
        elif categoria == "Longitud" and len(unidades) == 2:
            resultado = convertir_longitud(valor, unidades[0], unidades[1])
        # Agregar las demás categorías...

        # Mostrar el resultado
        st.write(f"{valor} {unidades[0]} es igual a {resultado:.2f} {unidades[1]}.")

if __name__ == "__main__":
    main()
