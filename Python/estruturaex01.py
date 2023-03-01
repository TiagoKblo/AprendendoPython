#Estruturas de dados - Listas
frutas = ['laranja','amora','morango','banana','amora','mamão','banana']
for fruta in frutas:
    print(fruta)

print("Quantidade de amoras:", frutas.count('amora'))
print("Quantidade de mangas:", frutas.count('manga'))
print("Quantidade de mamão:", frutas.index('mamão'))
#Adicionando um item a lista
print("Adicionando uva")
frutas.append('uva')
for fruta in frutas:
     print(fruta)
#Invertendo a lista
print("Invertende a lista")
frutas.reverse()
for fruta in frutas:
    print(fruta)
#Ordenando
print("Ordenando a lista")
frutas.sort()
for fruta in frutas:
    print(fruta)
