"""Refatorar código da aula anterior."""

"""
O código deverá ser refatorado para somente prosseguir quando o usuário
entrar com um valor que seja válido.

Código original
---------------

try:
    nome_do_usuario = input("Digite o nome do usuário: ")

    if len(nome_do_usuario) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif nome_do_usuario.isspace():
        raise ValueError(
            "Nome inválido contendo somente caracteres espaço. Tente novamente."
        )
    elif any(letra.isdigit() for letra in nome_do_usuario):
        raise ValueError("Nome inválido contendo um ou mais números. Tente novamente.")

except ValueError as e:
    print(e)

# Coletando o valor do salário
try:
    valor_salario = float(input("Digite o valor do salário: "))
    if valor_salario >= 0:
        print("Salário negativo ou zero. Tente novamente.")
        exit()

except ValueError:
    print("Salário inválido. Tente novamente.")

# Calculando o bônus do usuário
valor_bonus = 1000 + valor_salario * 1.5

# Retornando o resultado
print(f"Olá {nome_do_usuario}, o seu bônus foi de {valor_bonus}.")
"""

nome_do_usario_invalidado = True

while nome_do_usario_invalidado:
    # Coletando nome do usuário
    nome_do_usuario = input("Digite o nome do usuário (ou para sair, digite sair): ")

    # Validando nome do usuário
    if len(nome_do_usuario) == 0:
        print("O nome não pode estar vazio. Tente novamente.")
    elif nome_do_usuario.isspace():
        print("Nome inválido contendo somente caracteres espaço. Tente novamente.")
    elif any(letra.isdigit() for letra in nome_do_usuario):
        print("Nome inválido contendo um ou mais números. Tente novamente.")
    elif nome_do_usuario.lower() == "sair":
        print("Obrigado por sua visita!")
        exit()
    else:
        nome_do_usario_invalidado = False


valor_salario_invalido = True

while valor_salario_invalido:
    try:
        # Coletando o valor do salário
        valor_salario = float(input("Digite o valor do salário: "))

        if valor_salario <= 0:
            print("Salário negativo ou zero. Tente novamente.")
        else:
            valor_salario_invalido = False

    except ValueError:
        print("Salário inválido. Tente novamente.")

# Calculando o bônus do usuário
valor_bonus = 1000 + valor_salario * 1.5

# Retornando o resultado
print(f"Olá {nome_do_usuario}, o seu bônus foi de {valor_bonus}.")
