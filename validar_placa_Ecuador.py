import tkinter as tk
import re

# Definir las provincias y sus respectivas letras
provincias = {
    'Azuay': 'A', 'Bolívar': 'B', 'Carchi': 'C', 'Esmeraldas': 'E', 'Guayas': 'G', 'Chimborazo': 'H',
    'Imbabura': 'I', 'Santo Domingo de los Tsáchilas': 'J', 'Sucumbíos': 'K', 'Loja': 'L', 'Manabí': 'M',
    'Napo': 'N', 'El Oro': 'O', 'Pichincha': 'P', 'Orellana': 'Q', 'Los Ríos': 'R', 'Pastaza': 'S',
    'Tungurahua': 'T', 'Cañar': 'U', 'Morona Santiago': 'V', 'Galápagos': 'W', 'Cotopaxi': 'X', 'Santa Elena': 'Y', 'Zamora Chinchipe': 'Z'
}

# Definir la validación de letras según tipo de vehículo
# Vehículo Particular: segunda letra es una letra entre B y Y, EXCEPTO algunas letras específicas
letras_particular = set("BCDFGHIJKLNOPQRSTVWY")
# Vehículo de Servicio Público: segunda letra es una letra entre A y U, EXCEPTO algunas letras específicas
letras_servicio_publico = set("AUZEXM")
# Motocicleta: valida un formato diferente

# Reglas para las expresiones regulares de las placas
expresion_particular = r"^[A-Z][B-Y][A-Z]{2}\d{4}$"  # Vehículo particular (modificado)
expresion_moto = r"^[A-Z]{2}\d{3}[A-Z]$"  # Moto
expresion_servicio_publico = r"^[A-Z][A-U,Z,E,X,M][A-Z]{2}\d{4}$"  # Servicio público

# Letras válidas para la primera letra de la placa (correspondiente a las provincias)
letras_validas = set(provincias.values())

def verificar_placa():
    placa = entrada_placa.get()
    placa = placa.upper()  # Convertir la placa a mayúsculas para asegurarnos de que la validación funcione correctamente

    # Validar que la primera letra de la placa corresponde a una provincia válida
    if placa[0] not in letras_validas:
        resultado.set("La primera letra de la placa no corresponde a una provincia válida.")
        return

    # Validar placas de Carros particulares y Servicio Público con guión y longitud de 8 caracteres
    if len(placa) == 8 and '-' in placa:
        letras, numeros = placa.split('-')
        if len(letras) == 3 and len(numeros) == 4 and letras.isalpha() and numeros.isdigit():
            if placa[1] in letras_particular:
                provincia = [prov for prov, letra in provincias.items() if letra == placa[0]][0]
                resultado.set(f"La placa {placa} es de un vehículo Particular de la provincia {provincia} de Ecuador")
            elif placa[1] in letras_servicio_publico:
                provincia = [prov for prov, letra in provincias.items() if letra == placa[0]][0]
                resultado.set(f"La placa {placa} es de un vehículo de Servicio Público de la provincia {provincia} de Ecuador")
            else:
                resultado.set("La placa tiene formato incorrecto para Carro Particular o Servicio Público.")
        else:
            resultado.set("Formato incorrecto: Verifique que tenga 3 letras, un guion y 4 números.")
        return

    # Validar placa de moto con longitud de 6 caracteres y sin guión
    elif len(placa) == 6 and '-' not in placa:
        if re.match(expresion_moto, placa):
            provincia = [prov for prov, letra in provincias.items() if letra == placa[0]][0]
            resultado.set(f"La placa {placa} es de una Moto de la provincia {provincia} de Ecuador")
        else:
            resultado.set("Formato incorrecto para Moto: Verifique que tenga 2 letras, 3 números y 1 letra final.")
        return

    else:
        resultado.set("La placa no es válida según las reglas establecidas.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Verificación de Placa")
ventana.geometry("400x300")

# Crear los widgets
etiqueta_placa = tk.Label(ventana, text="Introduce la placa (Ej: AAT1234):")
etiqueta_placa.pack(pady=10)

entrada_placa = tk.Entry(ventana, font=("Arial", 14))
entrada_placa.pack(pady=10)

boton_verificar = tk.Button(ventana, text="Verificar", font=("Arial", 14), command=verificar_placa)
boton_verificar.pack(pady=20)

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
