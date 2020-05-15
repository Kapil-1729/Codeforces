def solve():
    n,a,b=map(int,input().split())
    s=""
    for i in range(97,97+b):
        s+=chr(i)
    res=""
    res+=(s)*(n//b)
    rem=n%b
    if rem!=0:
        res+=s[:rem]
    print(res)
 
t=int(input())
for loop in range(t):
    solve()
