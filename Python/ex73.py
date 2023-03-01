num = ['4','8','15','16','23','42']
print(num)
posicao = 0

while posicao < len(num):
    # logica
    numero = num[posicao]
    num[posicao] = int(numero) * 2

    posicao += 1

print(num)
