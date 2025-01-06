"""Exercício 7. Normalização de Dados em uma lista."""

try:
    LISTA_NUMEROS = [-100, 1, 200, 150, 160, 57, 98]

    minimo_lista = min(LISTA_NUMEROS)

    maximo_lista = max(LISTA_NUMEROS)

    diferenca_minimo_maximo = maximo_lista - minimo_lista

    lista_numeros_normalizada = []
    for numero in LISTA_NUMEROS:
        numero_normalizado = round((numero - minimo_lista) / diferenca_minimo_maximo, 2)
        lista_numeros_normalizada.append(numero_normalizado)

    print(f"A lista {LISTA_NUMEROS} após a normalização é {lista_numeros_normalizada}.")

except ValueError:
    print("Ocorreu um erro ao normalizar a lista. Revise os números e tente novamente.")
