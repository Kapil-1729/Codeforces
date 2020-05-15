def solve():
    l=[]
    for i in range(9):
        l.append(input())
    for i in range(9):
        l[i]=l[i].replace('2','1')
    for element in l:
        print(element)
 
t=int(input())
for loop in range(t):
    solve()
