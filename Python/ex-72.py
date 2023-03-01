letras = ['A','B','C','D','E']
print(letras)
letra = input("Digite a letra para substituir: ")

posicao = 0

for l in letras:
    if l == letra:
        letras[posicao] = 'X'
    posicao += 1
print(letras)

#letras = ['A','B','C','D','E']
#print(letras)
#letra_digitada = str(input("Qual letra voce deseja alterar por X:"))

#posicao = 0

#while posicao < len(letras):
    #letra = letras[posicao]
    #if letra == letra_digitada:
        #letras[posicao] = 'X'
    #43posicao += 1
