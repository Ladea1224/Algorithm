# from collections import deque

# #정확도 통과, 시간 초과(매번 다시 시추)
# def bfs(r,c,v,land,row,col):
#     v[r][c] = 1
#     cnt = 1
#     Q = deque([(r,c)])
#     while Q:
#         x,y = Q.popleft()
#         for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#             nx,ny = x+dx,y+dy
#             if not (0<=nx<row and 0<=ny<col): continue
#             if not land[nx][ny]: continue
#             if v[nx][ny]: continue
#             Q.append((nx,ny))
#             v[nx][ny] = 1
#             cnt += 1
#     return cnt
    
# def solution(land):
#     answer = 0
    
#     row, col = len(land), len(land[0])
#     for c in range(col):
#         v = [[0]*col for _ in range(row)]
#         cnt = 0
#         for r in range(row):
#             if not land[r][c]: continue
#             if v[r][c]: continue
#             cnt += bfs(r,c,v,land,row,col)
#             answer = max(answer,cnt)
#     return answer


# def bfs(k,r,c,stoneNum,land,row,col):
    
#     stoneNum[r][c] = k
#     cnt = 1
#     Q = deque([(r,c)])
#     while Q:
#         x,y = Q.popleft()
#         for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#             nx,ny = x+dx,y+dy
#             if not (0<=nx<row and 0<=ny<col): continue
#             if not land[nx][ny]: continue
#             if stoneNum[nx][ny]: continue
#             Q.append((nx,ny))
#             stoneNum[nx][ny] = k
#             cnt += 1
#     return cnt
    
#정보 저장 -> 정보 사용해서 계산 
# def solution(land):
#     row, col = len(land), len(land[0])
#     k = 1 #석유 번호
#     score = {} #석유 번호 -> 점수
#     stoneNum = [[0]*col for _ in range(row)] #위치 -> 석유 번호 (+방문 확인)
#     #정보 저장
#     for r in range(row):
#         for c in range(col):
#             if land[r][c] == 0: continue #시추 할 곳 아님
#             if stoneNum[r][c]: continue #이미 시추 하였음
#             score[k] = bfs(k,r,c,stoneNum,land,row,col) 
#             k+=1
#     #정답 계산
#     answer = 0
#     for c in range(col):
#         cnt = 0
#         v = set() #이번 열 케이스에서 시추한 번호
#         for r in range(row):
#             sn = stoneNum[r][c]
#             if not sn: continue
#             if sn in v: continue
#             cnt += score[sn]
#             v.add(sn)
#         answer = max(answer,cnt)
#     return answer
    
#관점 전환: 시추할 때 석유가 있었던 열에 각각 점수를 추가. 
#(방문 배열 따로 만들어도 되나, 재사용 할 일 없으므로 land 수정으로도 가능.)
from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    result = [0] * m  # 각 열(Column)별 최대 획득량 저장
    
    def bfs(a, b):
        count = 1
        land[a][b] = 0 # visited 대신 원본 배열을 0으로 만들어 방문 처리
        q = deque([(a, b)])
        
        min_y, max_y = b, b
        
        while q:
            x, y = q.popleft()
            
            # 현재 덩어리가 걸쳐 있는 최소/최대 열 업데이트
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                    land[nx][ny] = 0 # 방문 처리
                    q.append((nx, ny))
                    count += 1
                    
        # 덩어리가 걸쳐 있는 모든 열에 크기(count) 누적
        for i in range(min_y, max_y + 1):
            result[i] += count

    # 격자를 순회하며 석유를 발견하면 BFS 실행
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                bfs(i, j)
                
    return max(result)