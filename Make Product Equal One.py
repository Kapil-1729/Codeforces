n=int(input())
arr=list(map(int,input().split()))

countnegative=0
countzero=0
cost=0

for i in range(n):

    if arr[i]>0:
        cost+=(arr[i]-1)
        
    elif arr[i]<0:
        countnegative+=1
        cost+=(abs(arr[i])-1)

    else:
        countzero+=1

if countzero>0:
    cost+=countzero

else:
    if (countnegative%2)!=0:
        cost+=2

print(cost)
