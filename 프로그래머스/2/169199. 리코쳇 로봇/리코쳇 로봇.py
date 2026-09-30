from collections import deque

    
def solution(board):
    sr,sc,er,ec = 0,0,0,0    
    for i,line in enumerate(board):
        for j,X in enumerate(line):
            if X == "R":
                sr,sc = i,j
            if X == "G":
                er,ec = i,j
    
    
    Q = deque([(sr,sc)])
    vis = [ [-1]*len(board[0]) for _ in range(len(board))]
    vis[sr][sc] = 0
    while Q:
        x,y = Q.popleft()
        
        if (x,y) == (er,ec):
            return vis[x][y]
        
        for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            rx,ry = x,y
            while 0<=rx+dx<len(board) and 0<=ry+dy<len(board[0]) and board[rx+dx][ry+dy]!="D":
                rx,ry = rx+dx, ry+dy
            
            if vis[rx][ry]!=-1: continue
            
            vis[rx][ry] = vis[x][y] + 1
            Q.append((rx,ry))
            
    return -1
            
            
            
        
        
                
                