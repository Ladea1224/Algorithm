def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    
    pe = -1 #prev
    for target in targets:
        ns,ne = target #now
        if ns<pe: continue
        answer += 1
        pe = ne
        
    return answer