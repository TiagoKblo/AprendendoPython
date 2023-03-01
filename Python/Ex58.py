# Escreva um programa que receba o preço de dois produtos.
# Calcule um desconto de 14% no primeiro produto, 17% no segundo e
# exiba para o usuário o valor de cada produto e seus respectivos
# descontos.

prod1 = float ( input ("Escreva o valor do primeiro produto: R$ "))
prod2 = float ( input ("Escreva o valor do primeiro produto: R$ "))

totalprod = float (prod1 - (prod1 * (14/100)) + prod2 - (prod2 * (17/100)))
print ("Valor somado dos produtos: R$ ", totalprod)