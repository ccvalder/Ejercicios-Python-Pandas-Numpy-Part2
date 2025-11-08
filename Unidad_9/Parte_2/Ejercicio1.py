#Operación básica con NumPy: Utiliza la biblioteca NumPy para realizar las siguientes operaciones:

#Crea un array llamado vector con los números del 1 al 5.
#Calcula la media y la desviación estándar del array vector.
#Crea una matriz llamada matriz con 3 filas y 2 columnas, llenándola con números aleatorios entre 1 y 10.
#Multiplica todos los elementos de la matriz por 2.
#Muestra por pantalla el resultado de la multiplicación

import numpy as np
import pandas as pd

vector = np.array([1, 2, 3, 4, 5])


media = np.mean(vector)
desviacion = np.std(vector)

matriz = np.array([[7, 4],
                   [8, 5],
                   [7, 10]])

matriz_multiplicada = matriz * 2

df_resultado = pd.DataFrame(matriz_multiplicada, columns=["Columna1", "Columna2"])
print("Matriz Multiplicada:")
print(df_resultado.to_string(index=False))

