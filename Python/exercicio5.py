nome = str(input("Digite seu nome:"))
nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Parabéns", nome, "Você foi aprovado")
else:
    print("Você ficou com média:" ,media , "e foi reprovado")
