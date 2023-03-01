# Escreva um algoritmo que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O programa deve solicitaro 
# valor da cotação do dólar e a quantidade de dólares a ser convertido em reais.

valordolar = float (input ("Digite o valor da cotação do Dolar: US$ "))
totaldolar = float (input("Digite a quantidade de dinheiro em dolar US$ "))
totalreal = float (totaldolar*valordolar)
print("O valor total em reais é: R$", totalreal)