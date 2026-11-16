"""
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
    
"""
#리팩토링: directions 배열 사용, 이동하는 칸수 고정인 것 이용

def solution(n):
    tower = [[0] * n for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, -1)]

    r, c = -1, 0
    number = 1
    direction = 0

    for remaining in range(n, 0, -1):
        dr, dc = directions[direction]

        for _ in range(remaining):
            r += dr
            c += dc
            tower[r][c] = number
            number += 1

        direction = (direction + 1) % 3

    return [
        tower[r][c]
        for r in range(n)
        for c in range(r + 1)
    ]