"""Exercício 14. Tentativas de Conexão."""

try:
    maximo_tentativas = int(
        input("Digite a quantidade de tentativas de acesso que serão feitas: ")
    )
    if maximo_tentativas <= 0:
        raise ValueError(
            "Quantidade de tentativas deve ser um número interior maior que zero."
        )
except ValueError:
    print("Quantidade de tentativas inválida. Digite um número inteiro maior que zero.")

tentativa = 1

while tentativa <= maximo_tentativas:
    # Tente uma nova conexão
    print("Realizando tentativa de conexão...")
    resultado_conexao = False
    if resultado_conexao:
        print("Conexão realizada com sucesso!")
        break
    else:
        tentativa += 1
else:
    print("Não foi possível conectar.")
