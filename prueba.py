import re
import tkinter as tk
from tkinter import messagebox

# Diccionario de patrones para placas en Colombia
patrones_colombia = {
    'particular': re.compile(r"^[A-Z]{3}\s?\d{3}$"),   # Ejemplo: ABC 123 o ABC123
    'publico': re.compile(r"^[A-Z]{3}\s?\d{2}[A-Z]$")  # Ejemplo: ABC 12D o ABC12D
}

# Diccionario de patrones para placas en Ecuador
patrones_ecuador = {
    'particular': re.compile(r"^[A-Z]{1}\s?[A-Z]{1}\s?\d{3}$"),  # Ejemplo: A B 123 o AB 123
    'publico': re.compile(r"^[A-Z]{1}\s?[A-Z]{1}\s?\d{2}[A-Z]$")  # Ejemplo: A B 12D o AB 12D
}

# Mapeo de zonas en Colombia (Ejemplo ilustrativo)
zonas_colombia = {
    "AAA": "Zona Norte (Ej. Bogotá, Cundinamarca)",
    "BBB": "Zona Centro (Ej. Medellín, Antioquia)",
    "CCC": "Zona Sur (Ej. Cali, Valle del Cauca)",
    "DDD": "Zona Caribe (Ej. Barranquilla, Atlántico)",
    "EEE": "Zona Occidente (Ej. Manizales, Caldas)",
}

# Mapeo de provincias de Ecuador (primeras letras de la placa)
provincias_ecuador = {
    'A': 'Azuay',
    'B': 'Bolívar',
    'U': 'Cañar',
    'C': 'Carchi',
    'X': 'Cotopaxi',
    'H': 'Chimborazo',
    'O': 'El Oro',
    'E': 'Esmeraldas',
    'W': 'Galápagos',
    'G': 'Guayas',
    'I': 'Imbabura',
    'L': 'Loja',
    'R': 'Los Ríos',
    'M': 'Manabí',
    'V': 'Morona Santiago',
    'N': 'Napo',
    'S': 'Pastaza',
    'P': 'Pichincha',
    'Q': 'Orellana',
    'K': 'Sucumbíos',
    'T': 'Tungurahua',
    'Z': 'Zamora Chinchipe',
    'Y': 'Santa Elena',
    'J': 'Santo Domingo de los Tsáchilas'
}

# Función para analizar placas de Colombia
def analizar_placa_colombia(placa):
    placa = placa.upper().strip()
    
    # Identificar tipo de servicio
    if patrones_colombia['particular'].match(placa):
        tipo_servicio = "Particular"
    elif patrones_colombia['publico'].match(placa):
        tipo_servicio = "Público"
    else:
        return "Formato de placa desconocido"
    
    # Extraer las primeras tres letras de la placa para determinar la zona
    prefijo = placa[:3]
    zona = zonas_colombia.get(prefijo, "Zona desconocida")
    
    return f"Colombia: Tipo de servicio: {tipo_servicio}, Zona: {zona}"

# Función para analizar placas de Ecuador
def analizar_placa_ecuador(placa):
    placa = placa.upper().strip()
    
    # Identificar tipo de servicio
    if patrones_ecuador['particular'].match(placa):
        tipo_servicio = "Particular"
    elif patrones_ecuador['publico'].match(placa):
        tipo_servicio = "Público"
    else:
        return "Formato de placa desconocido"
    
    # Extraer la provincia de la placa
    provincia = placa[0]
    provincia_nombre = provincias_ecuador.get(provincia, "Provincia desconocida")
    
    return f"Ecuador: Tipo de servicio: {tipo_servicio}, Provincia: {provincia_nombre}"

# Función para identificar el país y analizar la placa
def analizar_placa(placa):
    placa = placa.strip()
    resultados = []
    
    if len(placa) == 0:
        return "Por favor ingrese una placa válida"
    
    # Comprobar si la placa coincide con Colombia
    resultado_colombia = None
    if patrones_colombia['particular'].match(placa) or patrones_colombia['publico'].match(placa):
        resultado_colombia = analizar_placa_colombia(placa)
    
    # Comprobar si la placa coincide con Ecuador
    resultado_ecuador = None
    if patrones_ecuador['particular'].match(placa) or patrones_ecuador['publico'].match(placa):
        resultado_ecuador = analizar_placa_ecuador(placa)
    
    # Si la placa coincide con ambos países
    if resultado_colombia and resultado_ecuador:
        return f"Esta placa podría pertenecer tanto a Colombia como a Ecuador.\n\n{resultado_colombia}\n{resultado_ecuador}"
    elif resultado_colombia:
        return resultado_colombia
    elif resultado_ecuador:
        return resultado_ecuador
    else:
        return "Formato de placa desconocido"

# Función para manejar el botón de verificación
def verificar_placa():
    placa = entry_placa.get()
    resultado = analizar_placa(placa)
    messagebox.showinfo("Resultado de la verificación", resultado)

# Configuración de la interfaz gráfica con tkinter
root = tk.Tk()
root.title("Verificación de Placa Vehicular")
root.geometry("400x200")

# Etiqueta para el texto introductorio
label = tk.Label(root, text="Ingrese la placa vehicular:", font=("Arial", 12))
label.pack(pady=10)

# Campo de entrada para ingresar la placa
entry_placa = tk.Entry(root, font=("Arial", 14))
entry_placa.pack(pady=5)

# Botón para verificar la placa
button = tk.Button(root, text="Verificar", command=verificar_placa, font=("Arial", 12))
button.pack(pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
