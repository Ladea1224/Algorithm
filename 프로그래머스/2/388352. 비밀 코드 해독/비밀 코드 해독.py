"""

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
"""
#리팩토링
#combinations(range(1,n+1),5) 로도 가능. (range 도 iterable)
#all 활용 ( for else 라는 문법도 있다.. for break 되지 않았으면 else 실행. 즉 flag 필요 없음)
from itertools import combinations
def solution(n, q, ans):
    answer = 0
    
    for case in combinations(range(1,n+1),5):
        caseSet = set(case)
        if all( len(caseSet & set(tQ))==tAns for tQ,tAns in zip(q,ans) ):
            answer+=1
            
    return answer

    
    
            
        
    
    
    