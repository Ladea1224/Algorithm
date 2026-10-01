def solution(m, n, startX, startY, balls):
    
    case1 = (startX,startY + (n-startY)*2)
    case2 = (startX,-startY)
    case3 = (-startX,startY)
    case4 = (startX + (m-startX)*2,startY) 
    cases = [case1,case2,case3,case4] #상하좌우
    
    result = []
    for ball in balls:
        r = 1e9
        for i,case in enumerate(cases):
            x,y = case
            bx,by = ball
            
            if bx==startX:
                if by>startY and i==0: continue
                if by<startY and i==1: continue
            if by==startY:
                if bx<startX and i==2: continue
                if bx>startX and i==3: continue
            
            r = min(r,(bx-x)*(bx-x) + (by-y)*(by-y))
        result.append(r)
    return result