inicio = int(input("Digite um valor: "))
fim = int(input("Digite o segundo valor: "))

if inicio > fim:
    inicio, fim = fim, inicio

for numero in range(inicio+1, fim):
    print(numero)




