n=int(input())
X=list(map(int,input().split()))
W=list(map(int,input().split()))
c=0
for i in range(n):
    c=c+(X[i]*W[i])/sum(W)
print("{:.1f}".format(c))
