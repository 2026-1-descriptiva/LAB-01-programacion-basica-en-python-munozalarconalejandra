"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    resultado = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split("\t")
            letra = parts[0]
            col5 = parts[4].split(",")

            suma = 0
            for item in col5:
                valor = int(item.split(":")[1])
                suma += valor

            resultado[letra] = resultado.get(letra, 0) + suma

    return resultado