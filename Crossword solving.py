def solve():
    n,m=map(int,input().split())
    s=input()
    t=input()
    result=[x for x in range(1,n+1)]
    for i in range(m-n+1):
        new_result=[]
        for j in range(n):
            if s[j]!=t[i+j]:
                new_result.append(j+1)
        if len(new_result)<len(result):
            result=new_result
    print(len(result))
    print(*result)
solve()
