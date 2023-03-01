# 61) Escreva um algoritmo que receba um nome e três notas e atenda
# exiba uma mensagem diferente para cada um dos casos a seguir:
# se média > 7 "Parabéns (nome)! Você foi aprovado"
# Se a média for menor que 7 e maior que 5, exiba a mensagem“
# Você ficou com média (media) e está de recuperação;
# Se a média for menor que 5, exiba a mensagem “(Nome), vocêestá reprovado”.

# Sem usar listas (método mais simples)
nome = input("Digite seu nome: ")
nota1 = float(input("Digite nota 1: ")) # float seria número real
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))

media = nota1 + nota2 + nota3

if media > 7:
    print("Parabéns ", nome, "! Você foi aprovado")
elif media > 5:
    print("Você ficou com média ", media, " e está de recuperação")
else:
    print(nome, ", você está reprovado")

# usando listas e laços de repetição
# acredito que ele provavelmente não cobre isso
nome = input("Digite seu nome: ")
notas = []
# você pode usar o valor fixo de 3
# ou guardar o limite em uma variável
limite = 3

for i in range(limite):
    # f"string", é um texto que posso colocar variáveis entre {  }
    # exemplo: f"Seu nome é : {nome}", é equivalente a "Seu nome é : " + nome
    nota = float(input(f"Digite nota {nota + 1}: "))
    notas.append(nota) # adiciona elemento ao final da lista

soma = 0

for nota in notas:
    soma += nota

media = soma / limite

if media > 7:
    print("Parabéns ", nome, "! Você foi aprovado")
elif media > 5:
    print("Você ficou com média ", media, " e está de recuperação")
else:
    print(nome, ", você está reprovado")
