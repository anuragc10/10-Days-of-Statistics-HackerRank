n=int(input())
P=list(map(int,input().split()))
F=list(map(int,input().split()))
L=[]
L1=[]
L2=[]
Q1=0
Q2=0
Q3=0

for j in range(n):
    while(F[j]>0):
        L.append(P[j])
        F[j]=F[j]-1

L.sort()
if(len(L)%2!=0):
    Q2=L[n//2]
    L1=L[:(len(L)//2)]
    if(len(L1)%2==0):
        Q1=(L1[len(L1)//2 -1]+L1[((len(L1))//2)])/2
    else:
        Q1=L1[len(L1)//2]
    L2=L[(len(L)//2)+1:]
    if(len(L2)%2==0):
        Q3=(L2[len(L2)//2 -1]+L2[((len(L2))//2)])/2
    else:
        Q3=L2[len(L2)//2]
    
else:
    L1=L[:(len(L)//2)]
    if(len(L1)%2==0):
        Q1=(L1[len(L1)//2 -1]+L1[((len(L1))//2)])/2
    else:
        Q1=L1[len(L1)//2]
    L2=L[(len(L)//2):]
    if(len(L2)%2==0):
        Q3=(L2[len(L2)//2 -1]+L2[((len(L2))//2)])/2
    else:
        Q3=L2[len(L2)//2]
        
print("{:.1f}".format(Q3-Q1))


