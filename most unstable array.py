def solve():
    n,m=map(int,input().split())
    if n==1:
        return 0
    elif n==2:
        return m
    else:
        return 2*m

t=int(input())
for loop in range(t):
    print(solve())
