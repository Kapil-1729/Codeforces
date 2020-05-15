def solve():
    n=int(input())
    k=n//2
    result=((k*(k+1)*((2*k)+1))/6)*8
    print(int(result))

t=int(input())
for loop in range(t):
    solve()
