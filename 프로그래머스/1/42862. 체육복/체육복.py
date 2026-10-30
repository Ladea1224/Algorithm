def solution(n, lost, reserve):
    answer = n
    
    rSet = set(reserve)-set(lost)
    
    for l in set(lost)-set(reserve):
        if l-1 in rSet:
            rSet.remove(l-1)
        elif l+1 in rSet:
            rSet.remove(l+1)
        else:
            answer-=1
        
    return answer