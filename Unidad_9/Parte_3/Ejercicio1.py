#Concatenación de DataFrames: Crea un programa que utilice Pandas para realizar las siguientes tareas:

#Crea dos DataFrames llamados df1 y df2 con las siguientes columnas: A, B, C.
#Llena ambos DataFrames con datos.
#Concatena verticalmente los dos DataFrames para crear un nuevo DataFrame llamado df_concat.
#Muestra por pantalla el resultado de la concatenación.


import pandas as pd


data1 = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df1 = pd.DataFrame(data1)


data2 = {
    'A': [10, 11, 12],
    'B': [13, 14, 15],
    'C': [16, 17, 18]
}

df2 = pd.DataFrame(data2)


df_concat = pd.concat([df1, df2])


print("DataFrame 1:")
print(df1.to_string(), "\n")

print("DataFrame 2:")
print(df2.to_string(), "\n")

print("Resultado de la Concatenación: ")
print(df_concat.to_string())
