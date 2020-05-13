def almost_equal():
    n=int(input())
    
    if n%2==0:
        print("NO")
        return
    
    print("YES")
    for i in range(1,n+1):
        if i%2==0:
            print(2*i,end=' ')
        else:
            print((2*i)-1,end=' ')
            
    for i in range(1,n+1):
        if i%2!=0:
            print(2*i,end=' ')
        else:
            print((2*i)-1,end=' ')
            
    print('')

almost_equal()
