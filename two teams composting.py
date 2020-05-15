def team():
    n=int(input())
    arr=list(map(int,input().split()))
    s=set(arr)
    
    if n==1:
        return 0
 
    if (len(s)==n):
        return 1
    
    d={}
    for element in arr:
        if element in d:
            d[element]+=1
        else:
            d[element]=1
    unique=len(s)
    max_key = 1
    for element in d:
        if d[element]>max_key:
            max_key=d[element]
    if unique==max_key:
        return unique-1
    res=min(max_key,unique)
    #if res>n//2:
        #return n//2
    return res
t=int(input())
for loop in range(t):
    print(team())
