def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

m,n=map(int,input().split())
print(factorial(min(m,n)))
