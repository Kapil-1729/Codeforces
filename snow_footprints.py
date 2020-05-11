def snow():
    n=int(input())
    S=input()

    if S.count('R')==0:
        s=S.rindex('L')+1
        t=S.index('L')

    else:
        s=S.index('R')+1
        if S.count('L')==0:
            t=S.rindex('R')+2
        else:
            t=S.rindex('R')+1

    print(s,t)

snow()
