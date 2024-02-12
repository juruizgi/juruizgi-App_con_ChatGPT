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

def convertir_peso_masa(valor, desde, hacia):
    conversiones = {
        ("Libras", "Kilogramos"): valor * 0.453592,
        ("Kilogramos", "Libras"): valor / 0.453592,
        ("Onzas", "Gramos"): valor * 28.3495,
        ("Gramos", "Onzas"): valor / 28.3495
    }
    return conversiones.get((desde, hacia), valor)

def convertir_volumen(valor, desde, hacia):
    conversiones = {
        ("Galones", "Litros"): valor * 3.78541,
        ("Litros", "Galones"): valor / 3.78541,
        ("Pulgadas cúbicas", "Centímetros cúbicos"): valor * 16.3871,
        ("Centímetros cúbicos", "Pulgadas cúbicas"): valor / 16.3871
    }
    return conversiones.get((desde, hacia), valor)

def convertir_tiempo(valor, desde, hacia):
    conversiones = {
        ("Horas", "Minutos"): valor * 60,
        ("Minutos", "Segundos"): valor * 60,
        ("Días", "Horas"): valor * 24,
        ("Semanas", "Días"): valor * 7
    }
    return conversiones.get((desde, hacia), valor)

def convertir_velocidad(valor, desde, hacia):
    conversiones = {
        ("Millas por hora", "Kilómetros por hora"): valor * 1.60934,
        ("Kilómetros por hora", "Metros por segundo"): valor / 3.6,
        ("Nudos", "Millas por hora"): valor * 1.15078,
        ("Metros por segundo", "Pies por segundo"): valor * 3.28084
    }
    return conversiones.get((desde, hacia), valor)

def convertir_area(valor, desde, hacia):
    conversiones = {
        ("Metros cuadrados", "Pies cuadrados"): valor * 10.764,
        ("Pies cuadrados", "Metros cuadrados"): valor / 10.764,
        ("Kilómetros cuadrados", "Millas cuadradas"): valor / 2.58999,
        ("Millas cuadradas", "Kilómetros cuadrados"): valor * 2.58999
    }
    return conversiones.get((desde, hacia), valor)

def convertir_energia(valor, desde, hacia):
    conversiones = {
        ("Julios", "Calorías"): valor / 4.184,
        ("Calorías", "Kilojulios"): valor * 4.184,
        ("Kilovatios-hora", "Megajulios"): valor * 3.6,
        ("Megajulios", "Kilovatios-hora"): valor / 3.6
    }
    return conversiones.get((desde, hacia), valor)

def convertir_presion(valor, desde, hacia):
    conversiones = {
        ("Pascales", "Atmósferas"): valor / 101325,
        ("Atmósferas", "Pascales"): valor * 101325,
        ("Barras", "Libras por pulgada cuadrada"): valor * 14.5038,
        ("Libras por pulgada cuadrada", "Bares"): valor * 0.0689476
    }
    return conversiones.get((desde, hacia), valor)

def convertir_tamano_datos(valor, desde, hacia):
    conversiones = {
        ("Megabytes", "Gigabytes"): valor / 1024,
        ("Gigabytes", "Terabytes"): valor / 1024,
        ("Kilobytes", "Megabytes"): valor / 1024,
        ("Terabytes", "Petabytes"): valor / 1024
    }
    return conversiones.get((desde, hacia), valor)

def main():
    st.title("Conversor Universal")

    # Seleccionar la categoría de conversión
    categoria = st.selectbox("Selecciona una categoría:", ["Temperatura", "Longitud", "Peso/masa", "Volumen", "Tiempo", "Velocidad","\n
                                                          "Área", "Energía", "Presión","Tamaño de datos"])

    # Seleccionar las unidades de conversión dentro de la categoría seleccionada
    if categoria == "Temperatura":
        unidades = st.multiselect("Selecciona las unidades:", ["Celsius", "Fahrenheit", "Kelvin"])
    elif categoria == "Longitud":
        unidades = st.multiselect("Selecciona las unidades:", ["Pies", "Metros", "Pulgadas", "Centímetros"])
    elif categoria == "Peso/masa":
        unidades = st.multiselect("Selecciona las unidades:", ["Kilogramos", "Libras", "Gramos", "Onzas"])

    # Ingresar el valor a convertir
    valor = st.number_input("Ingresa el valor a convertir:", value=0.0)

    # Realizar la conversión
    if st.button("Convertir"):
        resultado = valor  # Valor predeterminado si no hay conversión

        if categoria == "Temperatura" and len(unidades) == 2:
            resultado = convertir_temperatura(valor, unidades[0], unidades[1])
        elif categoria == "Longitud" and len(unidades) == 2:
            resultado = convertir_longitud(valor, unidades[0], unidades[1])
        elif categoria == "Peso/masa" and len(unidades) == 2:
            resultado = convertir_peso_masa(valor, unidades[0], unidades[1])

        # Mostrar el resultado
        st.write(f"{valor} {unidades[0]} es igual a {resultado:.2f} {unidades[1]}.")

if __name__ == "__main__":
    main()
