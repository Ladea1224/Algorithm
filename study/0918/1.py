#https://atcoder.jp/contests/abc026/tasks/abc026_c

#시간복잡도 = O(N)

import sys
sys.setrecursionlimit(10**6)

def money(num):
    unders = under[num]
    if len(unders) == 0:
        return 1
    elif len(unders) == 1:
        return money(unders[0])*2 + 1
    else:
        moneys = [money(x) for x in unders]
        return min(moneys)+max(moneys)+1

n = int(input())
under = [ list() for _ in range(n+1)] #under[k] = k번 직원의 부하 직원 리스트
for i in range(2,n+1):
    k = int(input())
    under[k].append(i)

print(money(1))


"""
2번째 풀이: 
# 템플릿 2: 트리 DP (Bottom-Up)
dp = [0] * (n + 1) # 결과를 저장할 DP 배열 (이 템플릿의 핵심)

def dfs(idx):
    # (트리는 단방향이므로 chk 배열 불필요)
    
    # 1. 말단 노드 처리
    if not under[idx]:
        dp[idx] = 1
        return
        
    # 2. 자식 노드들을 끝까지 파고듦
    moneys = []
    for next_node in under[idx]:
        dfs(next_node) # 일단 끝까지 내려보냄
        moneys.append(dp[next_node]) # 올라온 결과값을 수집
        
    # 3. 모인 자식들의 결과로 내(idx) 값을 계산해서 저장
    if len(moneys) == 1:
        dp[idx] = moneys[0] * 2 + 1
    else:
        dp[idx] = min(moneys) + max(moneys) + 1

dfs(1)
print(dp[1])
"""