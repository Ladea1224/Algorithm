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
#1,2,3,4 까지 작다가 1,2,3,4,5 에서 더 커졌다는 것은
#1. 1,2,3,4,5,6,... 뒤 볼 필요 없음(무조건 더 크기 때문)
#2. 2/ 2,3/ 2,3,4 볼 필요 없음(1,2,3,4 까지 더 작았으므로, 이것들도 무조건 더 작음)
#1,2를 볼 필요 없으므로, 2,3,4,5 부터 보기 시작하면 됨 = left 포인터 한칸 이동 한 것과 동일
def solution(n):
    answer = 0
    left,right = 1,1
    total = 1
    
    while left<=right:
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