"""
(풀이 2와 같이, 있는 그대로가 아니라 다른 표현 방식으로 생각해보는 연습 필요..)

#풀이 1: 있는 그대로. 시간대 별로 로봇이 움직인다고 생각.
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
"""
"""
#풀이 1-2: 이런 구현 문제는 기본적으로 시간보다 깔끔함을 우선 고려해서 작성..
# counter(딕셔너리) 사용하여 중복 카운트
# robot 배열 하나에 정보 전부 관리
# points 에 더미 넣어서 인덱스 처리
# 함수 대신 삼항 연산자로 이동 처리

from collections import Counter
def solution(points, routes):
    points = [None] + points
    x,m = len(routes),len(routes[0]) 
    answer = 0
    
    robots = [] # [r,c,다음 route idx, 전체 route 배열]
    for route in routes:
        r,c = points[route[0]]
        robots.append([r,c,1,route])
    
    counts = Counter((r,c) for r,c,_,_ in robots)
    answer += sum(1 for count in counts.values() if count>1)

    while robots:
        for robot in robots:
            r,c,rIdx,route = robot
            nr,nc = points[route[rIdx]]
            
            if r!=nr:
                robot[0] += 1 if r<nr else -1
            else:
                robot[1] += 1 if c<nc else -1
        
            if (robot[0],robot[1]) == (nr,nc):
                robot[2] += 1
                
        counts = Counter((robot[0], robot[1]) for robot in robots)
        answer += sum(1 for count in counts.values() if count > 1)
        
        robots = [robot for robot in robots if robot[2] < len(robot[3])]
                
    return answer
"""
#풀이2: 로봇마다 따로 진행하며 시공간별 정보 저장, 이후 한꺼번에 판단
from collections import Counter
def solution(points, routes):
    points = [None] + points
    inform = Counter()
    
    for route in routes:
        r,c = points[route[0]]
        t = 0
        inform[(t,r,c)] += 1
        
        ptr = 1 #다음 루트 ptr
        while ptr<len(route):
            nr,nc = points[route[ptr]]
            
            while r!=nr:
                r += 1 if r<nr else -1
                t += 1
                inform[(t,r,c)] += 1
            while c!=nc:
                c += 1 if c<nc else -1
                t += 1
                inform[(t,r,c)] += 1
            
            ptr += 1
            
    return sum(1 for cnt in inform.values() if cnt>1)
        
            
        
        
        
            
            
        
        
        
