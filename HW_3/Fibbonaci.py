n=int(input())
i=1
m=1
aux=0
cont=0
while cont<n-2 :
    aux=m
    m=i+m
    i=aux
    cont += 1
print(m)
