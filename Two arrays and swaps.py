def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    i=0
    j=n-1
    for q in range(k):
        if i==n or j==-1:
            break
        if a[i]<b[j]:
            a[i]=b[j]
            i+=1
            j-=1
    return sum(a)

t=int(input())
for loop in range(t):
    print(solve())
