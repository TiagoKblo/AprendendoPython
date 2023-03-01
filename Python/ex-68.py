sal = float(input("Digite seu salário R$:"))
if sal <= 1903:
  print("Voce é isento!")
elif sal <= 2826:
    print("Voce deve pagar R$",(sal*1.075-sal))
elif sal <= 3751:
    print("Voce deve pagar R$",(sal*1.15-sal))
elif sal >= 4464:
    print("Voce deve pagar R$",(sal*1.22-sal))


     #if sal in range(0,1903):
  #print("Voce é isento!")
#else:
    #if sal in range(1903,2826):
        #print("Voce deve pagar R$",(sal*1.075-sal))
    #else:
        #if sal in range(2826,3751):
            #print("Voce deve pagar R$",(sal*1.15-sal))
        #else:
            #if sal in range(3751,4464):
                #print("Voce deve pagar R$",(sal*1.22-sal))










