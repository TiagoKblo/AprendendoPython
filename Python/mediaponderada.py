n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
media = ((n1*3) + (n2*3) + (n3*4))/10
if media < 6:
    print("Você foi reprovado com média:",media)
else:
    print("Você foi aprovado com a média",media,"Parabéns!!")
