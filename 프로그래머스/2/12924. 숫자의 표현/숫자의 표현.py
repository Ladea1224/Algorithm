"""
# i=1, j 최대 150정도/ i=2, j 최대 150 이하, ... / i=5000쯤 부터는 바로바로 break
# 따라서 O(n^2) 보다 훨씬 적어서 통과 가능..
def solution(n):
    answer = 1
    for i in range(1,n+1):
        k = i
        for j in range(i+1,n+1):
            k+=j

            if k==n:
                answer+=1
                break
                
            if k>n:
                break
                
    return answer         
"""
#투포인터 O(n)
def solution(n):
    answer = 0
    left,right = 1,1
    total = 1
    
    while left<=right and right<=n:
        if total<n:
            right+=1
            total+=right
        if total==n:
            answer+=1
            total-=left
            left+=1
        if total>n:
            total-=left
            left+=1
            
    return answer