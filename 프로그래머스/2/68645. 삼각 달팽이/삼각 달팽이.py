# 수학이 아니라 배열로 봐서, 설명 그대로 넣기..

def solution(n):
    tower = [ [0]*i for i in range(1,n+1) ]
    
    r,c = 0,0
    dir,dr,dc = 0,1,0
    for i in range(1, (n*(n+1))//2 + 1):
        tower[r][c] = i
        
        if dir==0 and (r+dr>=n or tower[r+dr][c]):
            dr,dc = 0,1
            dir = 1
        elif dir==1 and (c+dc>=n or tower[r][c+dc]):
            dr,dc = -1,-1
            dir = 2
        elif dir==2 and tower[r+dr][c+dc]:
            dr,dc = 1,0
            dir = 0
        
        r,c = r+dr,c+dc
        
    return [x for sublist in tower for x in sublist]