# Escreva um algoritmo que receba 7 valroes digitados pelo usuário e no final exiba o maior número
cont = 0
maior = 0

while cont < 7:
    cont += 1
    numero = int (input("Entre com um número: "))
    if numero > maior:
        maior = numero

print ("O maior número é: ", maior)