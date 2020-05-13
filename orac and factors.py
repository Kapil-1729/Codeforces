def f(n):
    for i in range(2,n+1):
        if n%i==0:
            return i

def orac_factor():
    n,k=map(int,input().split())
    fn=f(n)
    print(fn+n+(k-1)*2)

t=int(input())
for loop in range(t):
    orac_factor()
