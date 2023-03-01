import random
#importa uma biblioteca para gerar números aleatórios

print("---------------------------")
print("    JOGO DE ADVINHAÇÃO     ")
print("---------------------------")

segredo = random.randrange(1,11)
print(segredo) # Número sorteado

acertou = False
tentativas = 3

for i in range (1, 4):
    print("Você possui" ,tentativas, "tentativas de 3\n")
    numero = int(input("Digite um número enttre 1 e 10: "))
    if numero >= 11:
        print("Valor inválido")

    if numero == segredo:
        acertou = True

    if acertou:
        print("--------------------------------")
        print("   VOCÊ ACERTOU!! PARABÈNS!!!   ")
        print("--------------------------------")
        break
    else:
        print("Você errou! O número sorteado foi:", segredo)
        tentativas -= 1
print("Fim de Jogo")        