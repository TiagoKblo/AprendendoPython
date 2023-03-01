t1 = int(input("Digite o primeiro termo:"))
qtd = int(input("Digite a quantidade de termos:"))
razao = int(input("Digite a razão:"))
for i in range(1,qtd+1):
    print("a",i,"...",t1)
    t1 = t1 + razao

