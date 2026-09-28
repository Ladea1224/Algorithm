from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for case in combinations([i for i in range(1,n+1)],5):
        possible = True
        for tQ,tAns in zip(q,ans):
            if len(set(case) & set(tQ))!=tAns:
                possible = False
                break
        if possible: answer+=1
    return answer
            
            
        
    
    
    