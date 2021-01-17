n=int(input())
L=list(map(int,input().split()))

u=sum(L)/n

for i in range(n):
    L[i]=(L[i]-u)**2
p=sum(L)/n
print("{:.1f}".format(p**(1/2)))
    
    
