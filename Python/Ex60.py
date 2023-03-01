# Escreva um algoritmo que receba um número inteiro e determine
# se ele e par ou ímpar. Dica: utilize o operador módulo (resto da
# divisão).

numero = int(input ("Digite um número: "))
calc = numero % 2

if calc == 0:
    print("O número digitado é Par")
else:
    print("O número digitado é Impar")
