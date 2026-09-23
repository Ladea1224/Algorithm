from bisect import bisect_left
def solution(sequence, k):
    result = []
    S = [0] #padding 넣었으므로, S[i] = i번째 원소까지 합(i>=1)
    for i in range(len(sequence)):
        S.append(S[i] + sequence[i])
    # left~right 부분 수열 합 = S[right] - S[left-1] = k
    # 따라서 S[right]-k = S[left-1] 인 right,left 가 곧 조건을 만족하는 부분 수열
    for right in range(1,len(sequence)+1):
        val = S[right]-k
        idx = bisect_left(S,val)
        #못찾았을 경우, 맨 오른쪽 끝이면 범위 벗어나므로 확인, 범위 안이라도 실제 찾은 위치인지, 못찾아서 정렬 유지하기 위한 위치(left)에 있는지 확인
        if idx < len(S) and S[idx] == val:
            result.append((idx,right-1)) #인덱스 기준으로 append
            
    
    #result 에서 우선순위에 따라 answer 정하기
    result.sort(key=lambda x:(x[1]-x[0],x[0]))
    
    return result[0]