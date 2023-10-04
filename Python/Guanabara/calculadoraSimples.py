while True:
    print("Bem vindo a Calculadora Simples")
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    operacao = input("Digite a operacao desejada, +, -, *, /: ")

    if operacao == "+":
        print("O resultado da soma eh: ", num1 + num2)
    elif operacao == "-":
        print("O resultado da subtracao eh: ", num1 - num2)
    elif operacao == "*":
        print("O resultado da multiplicacao eh: ", num1 * num2)
    elif operacao == "/":
        if num2 == 0:
            print("Erro: Divisao por zero!")
        else:
            print("O resultado da divisao eh: ", num1 / num2)
    else:
        print("Operacao invalida")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break

