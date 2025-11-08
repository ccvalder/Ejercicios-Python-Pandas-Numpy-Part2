#Manipulación básica con pandas: Crea un programa que utilice la biblioteca Pandas para realizar las siguientes tareas:

#Crear un DataFrame llamado datos con las siguientes columnas: Nombre, Edad, Ciudad.
#Mostrar por pantalla la información del DataFrame.
#Filtrar las filas donde la edad sea mayor que 25.
#Añadir una nueva columna llamada Categoría que clasifique a las personas en "Joven" si tienen 25 años o menos, y "Adulto" si tienen más de 25 años.
#Mostrar por pantalla el DataFrame actualizado.

import pandas as pd

datos = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "María", "Carlos"],
    "Edad": [22, 30, 25, 28],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
})
# Mostrar la información del DataFrame
print("Información del DataFrame:")
print(datos)
# Filtrar las filas donde la edad sea mayor que 25
filtro_edad = datos[datos["Edad"] > 25]
print("\nPersonas con edad mayor que 25:")
print(filtro_edad)
# Añadir una nueva columna llamada Categoría
datos["Categoria"] = datos["Edad"].apply(lambda x: "Joven" if x <= 25 else "Adulto")
# Mostrar el DataFrame actualizado
print("\nDataFrame Actualizado:")
print(datos)

