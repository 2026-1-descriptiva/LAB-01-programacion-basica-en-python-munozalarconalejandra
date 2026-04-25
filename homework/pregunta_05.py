"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split("\t")
            letra = parts[0]
            numero = int(parts[1])

            if letra not in valores:
                valores[letra] = [numero, numero]
            else:
                valores[letra][0] = max(valores[letra][0], numero)
                valores[letra][1] = min(valores[letra][1], numero)

    resultado = [(letra, vals[0], vals[1]) for letra, vals in valores.items()]
    return sorted(resultado)
