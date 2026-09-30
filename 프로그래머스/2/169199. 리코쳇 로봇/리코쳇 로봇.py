"""
1.리스트 컴프리헨션 쓰면 sr,sc = [(i,j) for ... for ... if ...] 두 줄로 끝나겠지만 board 두 번 돌아야 한다.. 성능 상 문제는 없겠지만 괜히 더 복잡한 느낌. 억지로 이런 방식 쓰지는 말자. 
even = [x for x in arr if x % 2 == 0] 과 같이 바로 필터링 하는 경우에만 쓰자


2.enumerate 쓸지 일반 i,j 쓸지... -> 타이핑 해보니 둘 다 비슷. 
근데 조금 더 편리한 enumerate 쓰자


3.도착 판정 시점 문제? -> 도착 판정은 무조건 큐에서 꺼낼 때 하자(큰 시간 차이 없을 것, 가독성 위해)


4. while 조건 표현 방식 고민 -> 정답은 없는 것 같다. 아래와 같은 여러 표현 방식중에 유동적으로 사용하되, 길게 고민하지말고 해보고 아니다 싶으면 다른 방식으로 틀자. 

- 내 코드. 안전 확인 후 이동 가능한만큼 이동한다. while 0 <= nx + dx < n ... and board[nx + dx][ny + dy] != 'D':
- 계속 하다가, 안되면 안가고 break한다. while True:  if not (안전범위) or board == 'D': break
- 안 되는 경우가 아니면 간다.(이게 제일 햇갈릴 수 있음) while not (nx + dx < 0 or ... or board == 'D'):
- 안될때까지 가고, 다시 한칸 돌아온다. while 0 <= nx < n ...: 하고 다 끝난 뒤에 nx -= dx; ny -= dy


"""



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
            
            

        
        
                
                