from collections import deque
"""
#정확도 통과, 시간 초과(매번 다시 시추)
def bfs(r,c,v,land,row,col):
    v[r][c] = 1
    cnt = 1
    Q = deque([(r,c)])
    while Q:
        x,y = Q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if not (0<=nx<row and 0<=ny<col): continue
            if not land[nx][ny]: continue
            if v[nx][ny]: continue
            Q.append((nx,ny))
            v[nx][ny] = 1
            cnt += 1
    return cnt
    
def solution(land):
    answer = 0
    
    row, col = len(land), len(land[0])
    for c in range(col):
        v = [[0]*col for _ in range(row)]
        cnt = 0
        for r in range(row):
            if not land[r][c]: continue
            if v[r][c]: continue
            cnt += bfs(r,c,v,land,row,col)
            answer = max(answer,cnt)
    return answer
"""

def bfs(k,r,c,stoneNum,land,row,col):
    
    stoneNum[r][c] = k
    cnt = 1
    Q = deque([(r,c)])
    while Q:
        x,y = Q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if not (0<=nx<row and 0<=ny<col): continue
            if not land[nx][ny]: continue
            if stoneNum[nx][ny]: continue
            Q.append((nx,ny))
            stoneNum[nx][ny] = k
            cnt += 1
    return cnt
    
def solution(land):
    row, col = len(land), len(land[0])
    k = 1 #석유 번호
    score = {} #석유 번호 -> 점수
    stoneNum = [[0]*col for _ in range(row)] #위치 -> 석유 번호 (+방문 확인)
    #정보 저장
    for r in range(row):
        for c in range(col):
            if land[r][c] == 0: continue #시추 할 곳 아님
            if stoneNum[r][c]: continue #이미 시추 하였음
            score[k] = bfs(k,r,c,stoneNum,land,row,col) 
            k+=1
    #정답 계산
    answer = 0
    for c in range(col):
        cnt = 0
        v = set() #이번 열 케이스에서 시추한 번호
        for r in range(row):
            sn = stoneNum[r][c]
            if not sn: continue
            if sn in v: continue
            cnt += score[sn]
            v.add(sn)
        answer = max(answer,cnt)
    return answer
    