n=int(input())
L=list(map(int,input().split()))
L1=[]
L2=[]
Q1=0
Q2=0
Q3=0
L.sort()

if(n%2!=0):
    Q2=L[n//2]
    L1=L[:(n//2)]
    if(len(L1)%2==0):
        Q1=(L1[len(L1)//2 -1]+L1[((len(L1))//2)])//2
    else:
        Q1=L1[len(L1)//2]
    L2=L[(n//2)+1:]
    if(len(L2)%2==0):
        Q3=(L2[len(L2)//2 -1]+L2[((len(L2))//2)])//2
    else:
        Q3=L2[len(L2)//2]
    
else:
    Q2=(L[n//2 -1]+L[(n//2)])//2
    L1=L[:(n//2)]
    if(len(L1)%2==0):
        Q1=(L1[len(L1)//2 -1]+L1[((len(L1))//2)])//2
    else:
        Q1=L1[len(L1)//2]
    L2=L[(n//2):]
    if(len(L2)%2==0):
        Q3=(L2[len(L2)//2 -1]+L2[((len(L2))//2)])//2
    else:
        Q3=L2[len(L2)//2]
        
    
print(Q1)
print(Q2)
print(Q3)
