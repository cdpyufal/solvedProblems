salario = float(input(""))
if (salario<1000):
    salario*=1.3
elif (salario<2000):
    salario*=1.1

print("%.2f" %(salario))
