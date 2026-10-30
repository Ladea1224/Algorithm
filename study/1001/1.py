# https://atcoder.jp/contests/abc153/tasks/abc153_e

"""
완탐은 말 안되고
그리디. 애매하긴한데 맞지않나? 특정 지점까지는 그냥 단순하게 효율 좋은거 계속 하다가 특정 지점부터 생각해봐야 하는데, 
이 특정 지점을 어떻게 정해야할지가 애매..
dp... 가장 간단  
 -> 하다가 dp 범위 H안쪽 아니라 넘어가도 되므로 H+A 하면 메모리 초과 문제.. 넘어가면 dp 기록은 안하고 바로 반영하고 넘어가기로
 -> 제출했는데 RE, WA
 -> 중간이 아니라 처음 세팅때도 H 초과할 수 있다 등 인덱스 문제 RE 해결(AI)
 -> WA는 여전히 모르겠어서 반례(AI), A가 같을 수 있음
 -> 애초에 아래 AI 코드처럼 0으로 출발했으면 초기 세팅 필요없었고 반례 생각도 필요없었다, 
    그리고 H 초과하는거 그냥 min(H,...) 인덱싱 해서 H쪽에 모을 수 있음
"""


H,N = map(int, input().split())

A,B= [],[]
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

d=[1e9]*(H)
ans = 1e9
for i in range(N):
    if A[i]>=H:
        ans=min(ans,B[i])
        continue
    d[A[i]] = min(d[A[i]],B[i])


for i in range(1,H):
    if d[i]==1e9: continue
    for j in range(N):
        idx,val = i+A[j],d[i]+B[j]
        if idx>=H:
            ans = min(ans,val)
            continue
        d[idx] = min(val,d[idx])

print(ans)



"""

import sys
input = sys.stdin.read

def solve():
    data = input().split()
    if not data: return
    
    H = int(data[0])
    N = int(data[1])
    
    A = []
    B = []
    idx = 2
    for _ in range(N):
        A.append(int(data[idx]))
        B.append(int(data[idx+1]))
        idx += 2
        
    # d[i] = 적의 체력을 i만큼 깎는 데 드는 최소 마력
    d = [1e9] * (H + 1)
    d[0] = 0  # 0의 데미지를 주는 데 드는 코스트는 0
    
    for i in range(H):
        if d[i] == 1e9: continue
        for j in range(N):
            # 다음 데미지가 H를 넘어가면 H로 제한 (Index out of range 방지)
            nxt = min(H, i + A[j])
            d[nxt] = min(d[nxt], d[i] + B[j])
            
    print(d[H])

solve()
"""