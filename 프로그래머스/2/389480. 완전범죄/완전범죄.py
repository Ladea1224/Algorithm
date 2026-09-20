"""
똑같은 순번에서 똑같은 결과에 도달했다면, 도달한 방법과 무관하게 이후 진행 과정은 동일하다.
따라서 특정 순번에서 특정 결과에 도달 가능한지 여부를 배열에 저장한다.
"""

def solution(info, n, m):
    infoCnt = len(info)
    dp = [[[False]*m for _ in range(n)] for _ in range(infoCnt+1)]
    dp[0][0][0] = True
    
    for i in range(infoCnt):
        A,B = info[i]
        for a in range(n):
            for b in range(m):
                if not dp[i][a][b]: continue
                
                if a+A < n:
                    dp[i+1][a+A][b] = True
                if b+B < m:
                    dp[i+1][a][b+B] = True
    
    return next( (a for a in range(n) for b in range(m) if dp[infoCnt][a][b]),-1)
    
