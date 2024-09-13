# Desafio: Criando um Sistema Bancário com Python
# Criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
# O sistema será desenvolvido para um banco que busca monetizar suas operações. 
# Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. 


menu = """
Escolha opção:

[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

"""

saldo = 0
limite_saque = 500.00
extrato = ""
numero_saque = 1
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Não é possível efetuar o depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        if valor > saldo:
            print(f"Saldo insuficiante, valor de saque R$ {valor} é menor que saldo R$ {saldo} em conta.")

        elif valor > limite_saque:
            print(f"O valor de saque em R$ {valor} é maior que o limite de R$ {limite_saque} permitido.")

        elif numero_saque > LIMITE_SAQUE:
            print("Limite de saque atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Valor inválido.")

    elif opcao == "e":
        if not extrato:
            print(f"Não houve movimentação bancária, saldo R$ {saldo:.2f}.")
        else:
            impressao = f"""
============= Extrato =============    
{extrato}
SALDO: R$ {saldo:.2f}
===================================
"""
            print(impressao)

    elif opcao == "q":
        print("Finalizando acesso.")
        break

    else:
        print("Opção inválida.")
