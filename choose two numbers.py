n=int(input())
arrn=list(map(int,input().split()))
m=int(input())
arrm=list(map(int,input().split()))
arrn.sort()
arrm.sort()
print(arrn[-1],arrm[-1])
