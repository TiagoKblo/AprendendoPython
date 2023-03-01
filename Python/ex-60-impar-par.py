# 60) Escreva um algoritmo que receba um número inteiro
# e determinese ele e par ou ímpar. Dica: utilize o operador módulo (resto dadivisão).

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

# Algumas referências usam 0 como "Neutro"
# então seria nesse caso

if numero % 2 == 0:
    print("Par")
elif numero != 0:
    print("Impar")
else:
    print("Neutro")
