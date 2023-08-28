menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def mostrar_mensagem_erro(mensagem):
    print("Operação falhou! " + mensagem)

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor <= 0:
                mostrar_mensagem_erro("Valor inválido! O valor deve ser maior que zero.")
            else:
                saldo += valor
                extrato += f"Depósito: R$ {valor}\n"
        except ValueError:
            mostrar_mensagem_erro("Valor inválido! Insira um número válido.")

    elif opcao == "s":
        try:
            valor = float(input("Digite o valor a ser sacado: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if valor <= 0:
                mostrar_mensagem_erro("Valor inválido! O valor deve ser maior que zero.")
            elif excedeu_saldo:
                mostrar_mensagem_erro("Saldo insuficiente!")
            elif excedeu_limite:
                mostrar_mensagem_erro("Limite excedido!")
            elif excedeu_saques:
                mostrar_mensagem_erro("Limite de saques excedido!")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor}\n"
                numero_saques += 1
        except ValueError:
            mostrar_mensagem_erro("Valor inválido! Insira um número válido.")

    elif opcao == "e":
        print("\n========== Extrato ==========")
        print("Não foram realizadas operações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================\n")

    elif opcao == "q":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida!")
