from sys import stdin, stdout 
def candy():
    n=int(stdin.readline())
    if (n%2)==0:
        res=(n//2)-1
    else:
        res=n//2
    stdout.write(str(res)+'\n')
 
t=int(input())
for loop in range(t):
    candy()
