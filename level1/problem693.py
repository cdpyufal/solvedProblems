P=[]
N=[]
valor=0
for i in range(0,3):
    P.append(float(input("")))
for i in range(0,3):
    N.append(int(input("")))
    valor += P[i]*N[i]

print("Valor: R$%.2f" %valor )
