def sail():
    t,sx,sy,ex,ey=map(int,input().split())
    if sx==ex and sy==ey:
        return 0
    time=0
    current=[sx,sy]
    instructions=input()
    for instruction in instructions:
        time+=1
        
        if instruction == 'N':
            if current[1]<ey:
                current[1]+=1
                
        if instruction == 'E':
            if current[0]<ex:
                current[0]+=1
        
        if instruction == 'S':
            if current[1]>ey:
                current[1]-=1

        if instruction == 'W':
            if current[0]>ex:
                current[0]-=1
        
        if current[0]==ex and current[1]==ey:
            return time

    return -1

print(sail())
