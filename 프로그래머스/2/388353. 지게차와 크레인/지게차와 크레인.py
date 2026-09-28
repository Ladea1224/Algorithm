from collections import deque

def isConn(storage,r,c):
    row, col = len(storage),len(storage[0])
    vis = [ [0]*col for _ in range(row)]
    q = deque([(r,c)])
    vis[r][c] = 1
    while q:
        x,y = q.popleft()
        if x==0 or x==row-1 or y==0 or y==col-1: return True
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if not (0<=nx<row and 0<=ny<col): continue
            if storage[nx][ny] != 0: continue
            if vis[nx][ny]: continue
            q.append((nx,ny))
            vis[nx][ny] = 1
            
    return False
        
    

def solution(storage, requests):
    storage = [list(row) for row in storage]
    
    for req in requests:
        target = req[0]
        
        if len(req)==2:
            storage = [ [x if x!=target else 0 for x in row ] for row in storage ]
        else:
            targetIdx = []
            for i,row in enumerate(storage):
                for j,x in enumerate(row):
                    if x==target and isConn(storage,i,j):
                        targetIdx.append((i,j))
                        
            for i,j in targetIdx:
                storage[i][j] = 0

    return sum(1 for row in storage for x in row if x!=0)