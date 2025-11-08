#DataFrame: Crea un programa que utilice la librería Pandas para crear un DataFrame con la siguiente información sobre 4 estudiantes: nombres, edades y calificaciones. Muestra el DataFrame resultante.

import pandas as pd

# Crear los datos en forma de diccionario
datos = {
    "Nombre": ["Ana", "Carlos", "María", "Juan"],
    "Edad": [20, 22, 21, 23],
    "Calificacion": [85, 90, 78, 95]
}

# Crear el DataFrame
df_estudiantes = pd.DataFrame(datos)

# Nuestra el DataFrame
print(df_estudiantes)