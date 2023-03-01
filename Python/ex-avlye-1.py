# Existe uma lista de [1, 2, 3, 666, 4, 5]
# Você deve substituir o valor 666 por 42
# E substituir o próximo valor por 42
num = [1,2,3,666,4,5]
pos = 0
for n in num:
    if n == 666:
        num[pos] = 42
        num[pos + 1] = 42
    pos += 1

print(num)
