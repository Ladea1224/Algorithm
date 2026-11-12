# 시간복잡도 ??
# 이중반복 X, k번째 행에만 놓으면 된다 (중복탐색 방지)

def solution(n):
    answer = 0
    
    p1,p2,p3,p4=set(),set(),set(),set() #행, 열, 증가 대각선, 감소 대각선
    def canPut(i,j):
        if i in p1: return False
        if j in p2: return False
        if i+j in p3: return False
        if i-j in p4: return False
        return True
    
    def dfs(k):
        nonlocal answer
        if k==n:
            answer+=1
            return
        
        i = k
        for j in range(n):
            if not canPut(i,j): continue

            p1.add(i)
            p2.add(j)
            p3.add(i+j)
            p4.add(i-j)
            dfs(k+1)
            p1.remove(i)
            p2.remove(j)
            p3.remove(i+j)
            p4.remove(i-j)
                
    dfs(0)
    
    
    dupl = 1
    
    return answer