def divisibility(a,b):
    if (a%b)==0:
        return 0
    else:
        return(b-(a%b))
 
t=int(input())
for loop in range(t):
    a,b=map(int,input().split())
    print(divisibility(a,b))
