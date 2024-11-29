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

    # Validar la placa según los tipos
    if placa[1] in letras_particular:
        provincia_letra = placa[0]
        provincia = [prov for prov, letra in provincias.items() if letra == provincia_letra][0]
        resultado.set(f"La placa {placa} es de un vehículo Particular de la provincia {provincia}.")
    elif placa[1] in letras_servicio_publico:
        provincia_letra = placa[0]
        provincia = [prov for prov, letra in provincias.items() if letra == provincia_letra][0]
        resultado.set(f"La placa {placa} es de un vehículo de Servicio público de la provincia {provincia}.")
    elif re.match(expresion_moto, placa):
        provincia_letra = placa[0]
        provincia = [prov for prov, letra in provincias.items() if letra == provincia_letra][0]
        resultado.set(f"La placa {placa} es de una Moto de la provincia {provincia}.")
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
