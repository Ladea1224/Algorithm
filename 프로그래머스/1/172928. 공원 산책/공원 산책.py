dict = {"N":[-1,0],
    "S":[1,0],
    "W":[0,-1],
    "E":[0,1]}
def move(park,route,pos):
    dir, cnt = route.split()
    cnt = int(cnt)
    nx, ny = pos
    dx, dy = dict[dir]
    for _ in range(cnt):
        nx,ny = nx+dx,ny+dy
        if( not (0<=nx<len(park)) or not (0<=ny<len(park[0])) ): return pos
        if(park[nx][ny] == "X"): return pos
    return [nx,ny]
    
def solution(park, routes):
    pos = next([i,row.index("S")] for i,row in enumerate(park) if "S" in row)
    
    for route in routes:
        pos = move(park,route,pos)
        
    return pos