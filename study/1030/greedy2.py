#https://school.programmers.co.kr/learn/courses/30/lessons/70130?language=python3

"""
모든 star 후보에 대해 각각 순회: 최악의 경우 O(N^2).

from collections import Counter

def solution(a):
    answer = 0
    counts = Counter(a)

    for x, count in counts.items():
        # x가 등장하는 횟수보다 많은 쌍은 만들 수 없음
        if count * 2 <= answer:
            continue

        pairs = 0
        i = 0

        while i < len(a) - 1:
            # 서로 다른 숫자이며 x가 포함된 쌍
            if a[i] != a[i + 1] and (a[i] == x or a[i + 1] == x):
                pairs += 1
                i += 2
            else:
                i += 1

        answer = max(answer, pairs * 2)

    return answer

"""

#한번 순회에 각 star 후보 경우를 모두 고려해서 저장하고, 최종적으로 판정: O(N)

from collections import Counter

def solution(a):
    cnts = Counter()
    last = Counter()    
    
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            continue
        
        for x in (a[i],a[i+1]):
            if i<last[x]: continue
            cnts[x] += 1
            last[x] = i+2   # [(1,2),1,2,3,..] 에서 i=0 일때 (1,2)를 사용했으므로, i=2 부터 봐야한다. (숫자가 다르면 다른 star 경우이므로 상관없음. 즉 last[x] 에서 안걸림.)
        
    return max(cnts.values(),default=0)*2
    
    
    
    