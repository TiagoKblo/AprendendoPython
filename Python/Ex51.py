nome = str (input("Digite seu nome: "))
nota1 = float (input("Digite a nota 1: "))
nota2 = float (input("Digite a nota 2: "))
nota = float ((nota1 + nota2)/2)
if nota >=7:
    print ("Parabéns {} ! Você foi aprovado" .format(nome))
else:
    print ("Você ficou com média {} e foi reprovado" .format(nota))