def getMove(r,c,nr,nc):
    if r<nr:
        return (1,0)
    if r>nr:
        return (-1,0)
    if c<nc:
        return (0,1)
    if c>nc:
        return (0,-1)
    else:
        return (0,0)

from copy import deepcopy
def solution(points, routes):
    answer = 0
     
    x = len(routes) #routes의 길이 = 로봇의 수
    m = len(routes[0]) #routes[i]의 길이(모두 같음)
    nrIdx = [1]*x #nrIdx[i] = i번 로봇이 가야 할 다음 route 에 대한 idx
    pos = [ deepcopy(points[route[0]-1]) for route in routes]
    
    start,danger = set(),set()
    for route in routes:
        rz = route[0]
        if (rz in start) and (rz not in danger):
            answer += 1
            danger.add(rz)
        start.add(rz)

    while any(idx != m for idx in nrIdx):
        arrive,danger = set(),set() # 이번에 도착한 위치, 위험 판정 위치
        for i in range(x): #i th robot
            if nrIdx[i]==m:      #다음 루트가 없는 경우
                continue

            r,c = pos[i] #현재
            nr,nc = points[routes[i][nrIdx[i]]-1] #가야하는 위치

            dr,dc = getMove(r,c,nr,nc)
            r,c = r+dr,c+dc #이동 후 현재
            pos[i] = [r,c]
            
            if (r,c) in arrive and (r,c) not in danger: #이미 누군가 도착했었고, 위험으로 카운트 되지 않음
                answer += 1
                danger.add((r,c))
            arrive.add((r,c)) 
        
            if (r,c) == (nr,nc): #도착 시, 다음 루트로
                nrIdx[i]+=1

    return answer