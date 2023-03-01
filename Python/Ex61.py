# Escreva um algoritmo que receba um nome e três notas e atenda
# exiba uma mensagem diferente para cada um dos casos a seguir:
# Se a média for maior que 7, exiba a mensagem “Parabéns
# (nome)! Você foi aprovado”;
# Se a média for menor que 7 e maior que 5, exiba a mensagem
# “Você ficou com média (media) e está de recuperação;
# Se a média for menor que 5, exiba a mensagem “(Nome), você
# está reprovado”.

nome = input ("Digite seu nome: ")
soma = 0.0

for i in range (0,3,1):
    nota = float (input (" Digite a nota {}: " . format(i+1)))
    soma += nota

media = soma / (i + 1)

print ("Sua média foi: ", media)

if media >= 7:
    print ("Parabéns {}! Você foi aprovado" . format(nome))
elif media < 7 and media >= 5:
    print ("Você ficou com média {} e está de recuperação" .format(media))
else:
    print ("{}, você está reprovado" .format(nome))




