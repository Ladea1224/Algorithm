# https://school.programmers.co.kr/learn/courses/30/lessons/62050?language=python3

# 학습: heap, 우선순위 큐, 완전이진트리, 최소신장트리(MST), 프림 알고리즘

# heap: 상위 노드가 하위 노드보다 작거나(최소 힙), 큰(최대 힙) 완전이진트리(트리 번호 순서대로 채움, 따라서 주로 배열로 구현)
# 추가(push) - 트리 번호 순에 맞게 두고, 거기서부터 swap 하면서 재조정(swap 마다 높이 하나씩 올라오므로 O(logN))
# 제거(pop) - 루트에서 뽑아감, 루트 자리에 마지막 번호였던 원소 놓고 swap 하면서 재조정(마찬가지 이유로 O(logN))   

# 우선순위 큐: 우선순위(주로 가장 크거나 작은)에 따라 pop 하는 큐. 구현을 위해 내부적으로 주로 heap 을 사용. 따라서 push/pop 에 O(logN)

# 최소신장트리(Min Spanning Tree): 그래프에서 간선 비용 합 최소 되도록 만든(spanning 한) 트리
# -> 어떻게 구하는가? = 프림 알고리즘 = 매 노드에서 최소비용인 간선을 선택한다
# 증명: 최소비용인 간선을 1, 아닌 간선을 2라고 할 때, 2를 선택해서 만들어진 MST가 있다고 하자,
# 이때 해당 MST에서 2를 제거하면 두덩어리로 나눠짐, 그리고 1로 바꿔 연결하면 다시 이어진다. (트리 성질에 의해)
# 즉 그대로 연결 유지했는데 비용이 줄어듬, 따라서 처음에 그런 MST가 있다는 것은 모순이다 -> 항상 최소 비용인 간선을 고르면 MST 가 만들어진다.
# -> 프림 알고리즘, 즉 매 노드에서 최소비용을 고르는 방법은? -> 우선순위 큐를 사용함.

"""
최초코드: 매번 candidate 정렬 (시간초과)

from collections import deque
dx=[0,0,-1,1]
dy=[-1,1,0,0]
def solution(land, height):
    answer = 0
    
    n = len(land)
    vis = [ [0]*n for _ in range(n)]
    
    Q = deque([(0,0)])
    vis[0][0] = 1
    visCnt = 1
    
    candi = []
    while visCnt<n*n:
        while Q:
            x,y = Q.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if not (0<=nx<n and 0<=ny<n): continue
                if vis[nx][ny]: continue
                
                diff = abs(land[nx][ny]-land[x][y])
                if diff>height:
                    candi.append((diff,nx,ny))
                    continue
                    
                Q.append((nx,ny))
                vis[nx][ny] = 1
                visCnt += 1
        
        # print(*vis,sep='\n')
        
        candi.sort(key=lambda x:x[0])
        # print(*candi)
        
        diff, nxt_x, nxt_y = 0,0,0
        for tdiff,tx,ty in candi:
            if vis[tx][ty]: continue
            diff, nxt_x, nxt_y = tdiff, tx,ty
            break
        
        # print(diff,nxt_x,nxt_y)
        
        Q.append( (nxt_x,nxt_y) )
        vis[nxt_x][nxt_y] = 1
        visCnt += 1
        
        answer += diff
    
    return answer

"""
# 배열 각 원소가 노드, 배열 간 이동 가능한 부분이 간선인 그래프에서 MST 구하기

import heapq
dx=[0,0,-1,1]
dy=[-1,1,0,0]
def solution(land, height):
    answer = 0
    n = len(land)
    vis = [ [0]*n for _ in range(n)]
    
    pq = [(0,0,0)] # 비용,row,col
    while pq:
        cost,x,y = heapq.heappop(pq)
        
        if vis[x][y]: continue
        
        vis[x][y] = 1
        answer += cost
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not (0<=nx<n and 0<=ny<n): continue
            if vis[nx][ny]: continue
            
            diff = abs(land[x][y] - land[nx][ny])
            next_cost = 0 if diff <= height else diff
            
            heapq.heappush(pq, (next_cost, nx, ny))
    
    return answer













