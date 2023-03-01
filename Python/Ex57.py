# Escreva um algoritmo que receba 5 valores digitados pelo usuário e no final exiba a média dos números.

cont = 0
calculado = 0.0
while cont < 5:
    cont += 1
    num = int (input("Entre com um número: "))
    calculado = calculado + num
calculado = calculado / cont
print ("A médiados núemros é: ", calculado)