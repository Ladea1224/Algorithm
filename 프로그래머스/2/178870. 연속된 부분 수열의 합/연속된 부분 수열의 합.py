from bisect import bisect_left
"""
#기존 
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
"""

"""#개선 및 관점 정리. (아래와 같이 이해 해도 되고, 아니면 그냥 case 하나 생각해봐서 맞춰가도 될 것 같다.)
def solution(sequence, k):
    S = [0]
    for num in sequence:
        S.append(S[-1]+num)
    
    answer = []
    min_len = 1e9
    # 문제 정의가 "S 배열 안에서 두 수의 차이가 k가 되는 짝 찾기" 로 바뀌었다. 따라서 right 는 S의 모든 원소가 될 수 있다는 의미상 len(sequence)+1 대신 len(S) 를 사용함. 이후에도 마찬가지 관점에서 이해하자.
    for right in range(1,len(S)):  
        target = S[right]-k # S[right] - S[left] = k 
        left = bisect_left(S,target) #sequence에서의 left가 아니라 그냥 지금 기준의, S에서 찾은 left라 생각해보자.
        if left<len(S) and S[left]==target:
            now_len = right-left # 여기에서는 sequence 관점으로 -> right 번째 원소까지 더해서 left 번째 원소까지 뺐다. 즉 부분수열의 길이는 right-left 이다. (사실 실제 부분 수열의 len과 다르더라도, 판정에는 영향이 없다)
            if now_len<min_len: # right 가 크기 순으로 탐색되므로, 같은 길이의 경우에는 먼저 발견된 경우의 left가 더 작은 것이 보장됨. 따라서 더 작은 길이의 경우에만 갱신한다.
                min_len = now_len
                answer = [left,right-1] # 여기에서도 sequence 관점으로 -> left = 버린 개수 = 시작 인덱스. 예를 들어 3개 버렸다면 2번 인덱스까지 버린 것이고, 시작 인덱스는 3. right는 더한 개수 였으므로, 5개 더했다면 인덱스 기준 4이므로 -1을 해준다.
    return answer
"""

#투포인터 풀이. 이미 본 정보를 바탕으로 일부 케이스를 제외할 수 있다. 예를 들어 (0,5)가 부족하고 (0,6)이 넘친다면, (1,6)부터 보면 된다. (0,5)가 부족했다는건 (n,5)는 전부 부족하다는 뜻이므로. right 옮기는 경우도 동일한 논리.
#정렬 배열이어야 할 필요 없음. 양수이면 됨. 양수를 추가하면 합은 무조건 커지고, 양수를 빼면 합은 무조건 작아지기 때문.

def solution(sequence, k):
    answer = []
    min_len = 1e9
    
    l,r,currSum = 0,0,sequence[0]
    n = len(sequence)
    while(r<n):
        if currSum<k:
            r+=1
            if r==n: break
            currSum += sequence[r]
            continue
        elif currSum>k:
            currSum -= sequence[l]
            l+=1
            continue
        else:
            now_len = r-l
            if now_len<min_len: # 이분탐색 풀이때와 마찬가지 이유로 같은 경우는 갱신 X, 작은 경우만 갱신함.
                min_len = now_len
                answer = [l,r]
            currSum -= sequence[l]
            l+=1
    return answer
    
    
                
            
