import tkinter as tk
from tkinter import messagebox
import re

# Diccionario con las reglas para vehículos particulares por estado
reglas_carros_particulares = {
    'AGUASCALIENTES': {'inicio': 'AAA-001-A', 'fin': 'AFZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Rojo'},
    'BAJA CALIFORNIA': {'inicio': 'AGA-001-A', 'fin': 'CYZ-999-Z', 'color_fondo': 'blanco, franja marrón', 'color_letra': 'negro'},
    'BAJA CALIFORNIA SUR': {'inicio': 'CZA-001-A', 'fin': 'DEZ-999-Z', 'color_fondo': 'blanco, franja verde', 'color_letra': 'negro'},
    'CAMPECHE': {'inicio': 'DFA-001-A', 'fin': 'DKZ-999-Z', 'color_fondo': 'blanco, franja colorida', 'color_letra': 'negro'},
    'COAHUILA': {'inicio': 'EUA-001-A', 'fin': 'FPZ-999-Z', 'color_fondo': 'blanco, franja negra', 'color_letra': 'verde'},
    'COLIMA': {'inicio': 'FRA-001-A', 'fin': 'FWZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'CHIAPAS': {'inicio': 'DLA-001-A', 'fin': 'DSZ-999-Z', 'color_fondo': 'blanco', 'color_letra': 'negro'},
   'CHIHUAHUA': {'inicio': 'DTA-001-A', 'fin': 'ETZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'azul'},
    'DURANGO': {'inicio': 'FXA-001-A', 'fin': 'GFZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Verde'},
    'GUANAJUATO': {'inicio': 'GGA-001-A', 'fin': 'GYZ-999-Z', 'color_fondo': 'Blanco, franja azul', 'color_letra': 'negro'},
    'GUERRERO': {'inicio': 'GZA-001-A', 'fin': 'HFZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'negro'},
    'HIDALGO': {'inicio': 'HGA-001-A', 'fin': 'HRZ-999-Z', 'color_fondo': 'Blanco, franja roja', 'color_letra': 'negro'},
    'JALISCO': {'inicio': 'HSA-001-A', 'fin': 'LFZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'negro'},
    'ESTADO DE MÉXICO': {'inicio': 'LGA-001-A', 'fin': 'PEZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'negro'},
    'MICHOACÁN': {'inicio': 'PFA-001-A', 'fin': 'PUZ-999-Z', 'color_fondo': 'Blanco, franja roja', 'color_letra': 'Negro'},
    'MORELOS': {'inicio': 'PVA-001-A', 'fin': 'RDZ-999-Z', 'color_fondo': 'Negro, con rojo', 'color_letra': 'Blanco'},
    'NAYARIT': {'inicio': 'REA-001-A', 'fin': 'RJZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'NUEVO LEÓN': {'inicio': 'RKA-001-A', 'fin': 'TGZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'OAXACA': {'inicio': 'THA-001-A', 'fin': 'TMZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'PUEBLA': {'inicio': 'TNA-001-A', 'fin': 'UJZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'QUERÉTARO': {'inicio': 'UKA-001-A', 'fin': 'UPZ-999-Z', 'color_fondo': 'Blanco, Franja azul', 'color_letra': 'Negro'},
    'QUINTANA ROO': {'inicio': 'URA-001-A', 'fin': 'UVZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'SAN LUIS POTOSÍ': {'inicio': 'UWA-001-A', 'fin': 'VEZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'SINALOA': {'inicio': 'VFA-001-A', 'fin': 'VSZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'SONORA': {'inicio': 'VTA-001-A', 'fin': 'WKZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'TABASCO': {'inicio': 'WLA-001-A', 'fin': 'WWZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'TAMAULIPAS': {'inicio': 'WXA-001-A', 'fin': 'XSZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'TLAXCALA': {'inicio': 'XTA-001-A', 'fin': 'XXZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'VERACRUZ': {'inicio': 'XYA-001-A', 'fin': 'YVZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'YUCATÁN': {'inicio': 'YWA-001-A', 'fin': 'ZCZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Negro'},
    'ZACATECAS': {'inicio': 'ZDA-001-A', 'fin': 'ZHZ-999-Z', 'color_fondo': 'Blanco', 'color_letra': 'Rojo'},
        # Agregar Ciudad de México
    'CIUDAD DE MÉXICO': {'inicio': 'A01-AAA', 'fin': 'Z99-ZZZ', 'color_fondo': 'Blanco', 'color_letra': 'Negro'}
}

# Diccionario con las reglas para motocicletas por estado
reglasMotocicletas = {
  "AGUASCALIENTES": [
    { 'inicio': 'N01AA', 'fin': 'N52LZ' },
    { 'inicio': 'A1AA1', 'fin': 'A9TL9' }
  ],
  "Baja California": [
    { 'inicio': 'N53LZ', 'fin': 'N05YZ' },
    { 'inicio': 'A1TM1', 'fin': 'B9KY9' }
  ],
  "Baja California Sur": [
    { 'inicio': 'N06YZ', 'fin': 'P57KY' },
    { 'inicio': 'B1KZ1', 'fin': 'C9DK9' }
  ],
  "Campeche": [
    { 'inicio': 'A01AA', 'fin': 'A99ZZ' },
    { 'inicio': 'C1DL1', 'fin': 'C9WX9' }
  ],
  "Chiapas": [
    { 'inicio': 'P58KY', 'fin': 'P10XY' },
    { 'inicio': 'C1WY1', 'fin': 'D9PJ9' }
  ],
  "Chihuahua": [
    { 'inicio': 'P11XY', 'fin': 'R62JY' },
    { 'inicio': 'D1PK1', 'fin': 'E9GW9' }
  ],
  "Coahuila": [
    { 'inicio': 'R63JY', 'fin': 'R15WY' },
    { 'inicio': 'E1GX1', 'fin': 'F9AH9' }
  ],
  "Colima": [
    { 'inicio': 'K01AA', 'fin': 'K99ZZ' },
    { 'inicio': 'F1AJ1', 'fin': 'F9TV9' }
  ],
  "EDO. de México": [
    { 'inicio': 'J01AA', 'fin': 'J99ZZ' },
    { 'inicio': 'G1NA1', 'fin': 'H9FL9' }
  ],
  "Durango": [
    { 'inicio': 'R16WY', 'fin': 'S67HX' },
    { 'inicio': 'H1FM1', 'fin': 'H9YY9' }
  ],
  "Guanajuato": [
    { 'inicio': 'S68HX', 'fin': 'S20VX' },
    { 'inicio': 'H1YZ1', 'fin': 'J8XK4' }
  ],
  "Guerrero": [
    { 'inicio': 'S21VX', 'fin': 'T72GY' },
    { 'inicio': 'J8XK5', 'fin': 'K9JX9' }
  ],
  "Hidalgo": [
    { 'inicio': 'T73GY', 'fin': 'T25UY' },
    { 'inicio': 'K1JY1', 'fin': 'L9CJ9' }
  ],
  "Jalisco": [
    { 'inicio': 'M01AA', 'fin': 'M99ZZ' },
    { 'inicio': 'L1CK1', 'fin': 'L9VW9' }
  ],
  "Michoacán": [
    { 'inicio': 'D01AA', 'fin': 'D99ZZ' },
    { 'inicio': 'L1VX1', 'fin': 'M9NH9' }
  ],
  "Morelos": [
    { 'inicio': 'T26UY', 'fin': 'U77FX' },
    { 'inicio': 'M1NJ1', 'fin': 'N9FV9' }
  ],
  "Nayarit": [
    { 'inicio': 'U78FX', 'fin': 'U30TX' },
    { 'inicio': 'N1FW1', 'fin': 'N9ZG9' }
  ],
  "Nuevo León": [
    { 'inicio': 'U31TX', 'fin': 'V82EW' },
    { 'inicio': 'N1ZH1', 'fin': 'P9SU9' }
  ],
  "Oaxaca": [
    { 'inicio': 'E01AA', 'fin': 'E99ZZ' },
    { 'inicio': 'P1SV1', 'fin': 'R9KF9' }
  ],
  "Puebla": [
    { 'inicio': 'F01AA', 'fin': 'F99ZZ' },
    { 'inicio': 'R1KG1', 'fin': 'S9CT9' }
  ],
  "Querétaro": [
    { 'inicio': 'V83EW', 'fin': 'V35SW' },
    { 'inicio': 'S1CU1', 'fin': 'S9WE9' }
  ],
  "Quintana Roo": [
    { 'inicio': 'B01AA', 'fin': 'C99ZZ' },
    { 'inicio': 'S1WF1', 'fin': 'T9NS9' }
  ],
  "San Luis Potosí": [
    { 'inicio': 'V36SW', 'fin': 'W87DV' },
    { 'inicio': 'T1NT1', 'fin': 'U9GD9' }
  ],
  "Sinaloa": [
    { 'inicio': 'H01AA', 'fin': 'H99ZZ' },
    { 'inicio': 'U1GE1', 'fin': 'U9ZR9' }
  ],
  "Sonora": [
    { 'inicio': 'W88DV', 'fin': 'W40RV' },
    { 'inicio': 'U1ZS1', 'fin': 'V9TC9' }
  ],
  "Tabasco": [
    { 'inicio': 'W41RV', 'fin': 'X92CU' },
    { 'inicio': 'V1TD1', 'fin': 'W9KP9' }
  ],
  "Tamaulipas": [
    { 'inicio': 'X93CU', 'fin': 'X45PU' },
    { 'inicio': 'W1KR1', 'fin': 'X9DB9' }
  ],
  "Tlaxcala": [
    { 'inicio': 'X46PU', 'fin': 'Y97BT' },
    { 'inicio': 'X1DC1', 'fin': 'X9WN9' }
  ],
  "Veracruz": [
    { 'inicio': 'Y98BT', 'fin': 'Y50NT' },
    { 'inicio': 'X1WP1', 'fin': 'Y9PA9' }
  ],
  "Yucatán": [
    { 'inicio': 'Y51NT', 'fin': 'Z03AT' },
    { 'inicio': 'Y1PB1', 'fin': 'Z9GM9' }
  ],
  "Zacatecas": [
    { 'inicio': 'L01AA', 'fin': 'L99ZZ' },
    { 'inicio': 'Z1GN1', 'fin': 'Z9ZZ9' }
  ]
};



# Función para verificar el tipo de vehículo y estado según la placa
def verificar_placa():
    placa = entry_placa.get()  # Obtener el valor ingresado en el campo de texto

    # Validar el formato de la placa para carros particulares
    patron_carro_particular = re.compile(r'^[A-Z]{3}-\d{3}-[A-Z]$')
    patron_motocicleta = re.compile(r'^[M][A-Z]{2}-\d{3}-[A-Z]$')
    patron_ciudad_de_mexico = re.compile(r'^[A-Z]\d{2}-[A-Z]{3}$')
    
    if patron_carro_particular.match(placa):
        # Extraer las letras de la placa para determinar el estado
        estado = determinar_estado_carro(placa)
        if estado:
            resultado = f"El vehículo es un carro particular en el estado de {estado}. " \
                       f"Color de fondo: {reglas_carros_particulares[estado]['color_fondo']}. " \
                       f"Color de letra: {reglas_carros_particulares[estado]['color_letra']}."
        else:
            resultado = "Estado no encontrado para esta placa."
    
    elif patron_motocicleta.match(placa):
        # Verificar si es una placa de motocicleta
        estado = determinar_estado_motocicleta(placa)
        if estado:
            resultado = f"El vehículo es una motocicleta en el estado de {estado}. " \
                       f"Color de fondo: {reglasMotocicletas[estado]['color_fondo']}. " \
                       f"Color de letra: {reglasMotocicletas[estado]['color_letra']}."
        else:
            resultado = "Estado no encontrado para esta placa de motocicleta."


    elif patron_ciudad_de_mexico.match(placa):
        # Verificar si es una placa de la Ciudad de México
        estado = 'CIUDAD DE MÉXICO'
        resultado = f"El vehículo es un carro particular en el estado de {estado}. " \
                   f"Color de fondo: {reglas_carros_particulares[estado]['color_fondo']}. " \
                   f"Color de letra: {reglas_carros_particulares[estado]['color_letra']}."
    else:
        resultado = "Formato de placa no válido para un carro particular."
    
    # Mostrar el resultado en un cuadro de mensaje
    messagebox.showinfo("Resultado", resultado)

# Función para determinar el estado del vehículo con base en la placa
def determinar_estado_carro(placa):
    for estado, reglas in reglas_carros_particulares.items():
        # Extraemos la parte inicial y final de la placa
        serie_inicial = reglas['inicio']
        serie_final = reglas['fin']

        # Verificamos si la placa está dentro del rango
        if esta_dentro_del_rango(placa, serie_inicial, serie_final):
            return estado
    return None

#Función para determinar el estado del vehículo con base en la placa de motocicleta
def determinar_estado_motocicleta(placa):
    for estado, reglas in reglasMotocicletas.items():
        # Extraemos la parte inicial y final de la placa
        serie_inicial = reglas['inicio']
        serie_final = reglas['fin']

        # Verificamos si la placa está dentro del rango
        if esta_dentro_del_rango(placa, serie_inicial, serie_final):
            return estado
    return None

# Función para verificar si la placa está dentro del rango de la serie
def esta_dentro_del_rango(placa, serie_inicial, serie_final):
    # Convertir las letras a su valor alfabético y los números a su valor numérico
    placa_num = convertir_placa_a_num(placa)
    serie_inicial_num = convertir_placa_a_num(serie_inicial)
    serie_final_num = convertir_placa_a_num(serie_final)
    
    return serie_inicial_num <= placa_num <= serie_final_num

# Función para convertir la placa a un valor numérico
def convertir_placa_a_num(placa):
    num = 0
    for char in placa:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char.isalpha():
            num = num * 26 + (ord(char) - ord('A') + 1)
    return num

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Verificador de Placas de Vehículos")

# Crear los widgets
etiqueta_instruccion = tk.Label(ventana, text="Ingresa la placa del vehículo:")
etiqueta_instruccion.pack(pady=10)

entry_placa = tk.Entry(ventana, width=20)
entry_placa.pack(pady=10)

boton_verificar = tk.Button(ventana, text="Verificar Placa", command=verificar_placa)
boton_verificar.pack(pady=20)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
