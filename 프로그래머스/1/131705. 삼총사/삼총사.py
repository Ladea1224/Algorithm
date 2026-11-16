def solution(number):
    answer = 0
    
    def dfs(k,sum,idx):
        nonlocal answer
        if k==3:
            if sum==0:
                answer+=1
            return
        
        for i in range(idx,len(number)):
            dfs(k+1,sum+number[i],i+1)
        
            
    dfs(0,0,0) # 개수, sum, idx
    
    return answer