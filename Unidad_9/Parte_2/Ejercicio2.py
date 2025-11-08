#Crea un programa que utilice Pandas para realizar las siguientes tareas:

#Generar manualmente un conjunto de datos simulando el conjunto de datos de Iris.
#Cargar los datos en un DataFrame llamado iris, incluyendo las siguientes columnas:
#sepal_length (longitud del sépalo)
#sepal_width (ancho del sépalo)
#petal_length (longitud del pétalo)
#petal_width (ancho del pétalo)
#species (especie de la flor)
#Mostrar las primeras 5 filas del DataFrame.
#Filtrar las filas donde la especie sea "Iris-setosa".
#Calcular la media de la longitud de los sépalos (sepal_length) para las filas filtradas.
#Mostrar los resultados en formato tabular.


import pandas as pd


data = {
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal_width':  [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal_width':  [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': [
        'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
        'Iris-setosa', 'Iris-setosa'
    ]
}

iris = pd.DataFrame(data)


print("Primeras 5 Filas del DataFrame: ")
print(iris.head().to_string(index=False), "\n")

iris_setosa = iris[iris['species'] == 'Iris-setosa']

print("Filtrado - Solo Iris-setosa: ")
print(iris_setosa.to_string(index=False), "\n")

media_sepal_length = iris_setosa['sepal_length'].mean()

resultado = pd.DataFrame({
    'Media sepal_length': [media_sepal_length]
})

print(f"Media de la longitud de los sépalos para 'Iris-setosa': {media_sepal_length:.2f}\n")

