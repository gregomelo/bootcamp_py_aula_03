"""Exercício 11. Leitura de Dados até Flag."""

dados_entrada = []
entrada = ""

while entrada != "sair":
    entrada = input("Digite um novo dado (ou sair para terminar): ")
    if entrada.lower() != "sair":
        dados_entrada.append(entrada)
