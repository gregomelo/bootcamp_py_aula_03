"""Exercício 1: Verificação de Qualidade de Dado."""

"""
Você está analisando um conjunto de dados de vendas e precisa garantir
que todos os registros tenham valores positivos para `quantidade` e `preço`.
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
forem positivos ou "Dados inválidos" caso contrário.
"""
try:
    valor_quantidade = float(input("Digite a quantidade vendida: "))

    valor_preco = float(input("Digite o valor vendido: "))

    if valor_quantidade > 0 and valor_preco > 0:
        print("Dados válidos.")
    else:
        raise ValueError("Dados inválidos.")
except ValueError:
    print("Dado de entrada inválido. Tente novamente.")
