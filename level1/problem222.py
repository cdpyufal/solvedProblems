a = []
for x in input().split():
    a.append(int(x))

pCor=(a[0]*3+a[1]*1)
pFla=(a[3]*3+a[4]*1)

saldoC=int(a[2])
saldoF=int(a[5])

if pCor>pFla:
    print("C")
elif pCor<pFla:
    print("F")
else:
    if saldoC>saldoF:
        print("C")
    elif saldoC<saldoF:
        print("F")
    else:
        print("=")
