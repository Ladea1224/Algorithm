from collections import deque
# 시간대 별 서버 수 배열 만들 수도 있음. 예를들어 t=3 에 증설했다면 3,4,5,6,7에 서버 개수 추가 되는 방식
def solution(players, m, k):
    answer = 0
    
    server = 0
    q = deque()
    for t,player in enumerate(players):
        
        if q and q[0][0]==t:
            server -= q[0][1] 
            q.popleft()
            
        need = player//m
        
        if server>=need: continue
        
        answer += need-server
        q.append((t+k,need-server)) #(시간,개수)
        server = need
    
    return answer