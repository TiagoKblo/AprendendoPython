# Escreva um algoritmo que carregue uma lista com seis números
# informe para o usuário qual o maior número e em qual posição
# lista ele se encontra

print ("Lista de números")
numeros = [1,4,3,6,2,5]
maior = 0
posicao = 0

for i in range(0,6,1):
    print (numeros[i])
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i + 1
print ("O maior numero é {} e ele está na posicação {} da lista" .format(maior,posicao))
