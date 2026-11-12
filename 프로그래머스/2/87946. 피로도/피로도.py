# O(8!) 이므로 완전탐색
# 근데 그리디 아닌가? 현재 가능한 던전중에 소모가 가장 적은 곳 가는게 이득?

def solution(k, dungeons):
    answer = -1
    NEED,USE = 0,1 # dungeons[row][NEED], dungeons[row][USE]
    
    vis = [0]*len(dungeons)
    def dfs(cnt,k):
        nonlocal answer
        answer = max(answer,cnt)
        
        for i in range(len(dungeons)):
            if vis[i]: continue
            if dungeons[i][NEED]>k: continue
            vis[i] = 1
            dfs(cnt+1, k-dungeons[i][USE])
            vis[i] = 0
            
    dfs(0,k) # 방문 던전 수, 피로도
    return answer