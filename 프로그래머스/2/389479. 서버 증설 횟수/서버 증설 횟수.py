from collections import deque

def solution(players, m, k):
    answer = 0
    
    server = 0
    t,q = -1,deque()
    for player in players:
        t+=1
        
        if q and q[0][0]==t:
            server -= q[0][1] 
            q.popleft()
            
        need = player//m
        
        if server>=need: continue
        
        answer += need-server
        q.append((t+k,need-server)) #(시간,개수)
        server = need
    
    return answer