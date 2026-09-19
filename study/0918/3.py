#https://atcoder.jp/contests/adt_all_20240320_1/tasks/abc268_d
from itertools import permutations
import sys
sys.setrecursionlimit(10**6)

#WA 원인: 엣지케이스
#TLE 원인: 문자열 무거운 연산 반복 + 가지치기 안해서.
"""
백트래킹(재귀)에서 시간 복잡도 계산 관련

recur():
    if(최대 재귀 깊이) ...
    for(반복 횟수):
        recur():

기본적으로 위와 같은 구조라면
재귀 한번 당 10번 호출 하므로, (반복 횟수)^(재귀 깊이) 만큼 연산 일어남.

예를 들어 깊이=5, 반복=10 이라고 하면, 10^5번. (수형도를 생각해보면 된다. 한번 뻗어나갈 때 10개 뻗어나가고, 뻗어나가는 횟수가 5인 상황임)
(참고로 2번 문제에서는 한번 뻗어나갈 때 이전 방문한 위치는 제외했으므로, 10*9*... 해서 10! 과 같이 계산 됐었다.)

**그러나 조건에 따라 가지치기 되는 경우에는 그 수가 크게 줄어든다.**

따라서(일반적으로는 코드를 보고 계산하는 것과 달리) 수학적 계산으로 실질적인 재귀 호출 횟수, 시간복잡도 등을 가늠해야 한다.

처음 시간 초과 했던 코드의 경우 = 자연수 합쳐서 8이 되는 상황을 만들어야 하므로, 2^8 정도로 계산됨.
(수학적 직관이 필요하므로 계산 어려울 수 있음. 모르겠다면 해당 부분만 따로 만들어서 돌려볼 수도 있다. test.py 참조)

**중요한 것은, 재귀에서는 가지치기가 시간에 매우 큰 영향을 줄 수 있다는 것이다.**


요약:
기본적으로는 (반복 횟수)^(재귀 깊이) 만큼 연산 일어난다. 그러나 가지치기 등에 의해 연산 수가 크게 바뀔 수 있다.
따라서 수학적으로 가늠해야 한다. 
그것도 어려운데 그냥 완전탐색이 맞다고 보이는 경우, 가지치기 등 최적화를 최대한으로 하자. 시간초과에 큰 영향을 미친다.

이 문제에서는: 
가능한 문자열을 경우의 수로 따져 봤을 때, dfs로 전부 만들어도 시간 내에 가능하다는 걸 알 수 있음.
단, 가지치기 완벽하게 해서 불필요한 탐색을 안했을 때의 경우이므로, 가지치기를 제대로 해줬어야 했다.

    
"""

#추가적으로 리팩토링 한다면: base_len과 used를 인자로 넘겨주어 불필요한 연산 반복을 제거할 수 있겠다.
def rec(case,underbars):  # case = [ab,cd,ef,gh]
    #이미 발견
    global flag
    if flag: return

    #리팩토링: case 안의 글자 수 변수 하나로 빼놓기. (매번 join 계산하지 않도록)
    base_len = sum(map(len, case))

    #글자 수 초과
    used = sum(underbars)
    remain = len(case) - 1 - len(underbars) #리팩토링: 남은 칸수(언더바 들어갈 자리) 또한 언더바를 최소 1개씩 가지므로, 해당 개수도 미리 예상하여 전체 길이가 16을 넘는지 확인한다.
    if base_len+used+remain > 16:
        return

    #문자 만들고 확인
    if len(underbars) == len(case)-1:
        result = ""
        for i in range(len(case)-1):
            result += case[i]
            result += "_" * underbars[i]
        result += case[-1]

        if len(result)<3: #단어 하나만 있는 경우는, 언더바 붙일 수 없으므로 길이가 3 이하일 수 있다. (엣지케이스)
            return

        if result not in T:
            print(result)
            flag = True
            return
        else:
            return

    max_i = 16 - base_len - used - (remain - 1) #리팩토링: 언더바 가능 개수 i <= 16 - base_len(글자수) - used(언더바 수) - (remain - 1)(남은 언더바 입력 칸 수) 이므로. 탐색 범위를 구체적으로 제한함
    for i in range(1,max_i+1): 
        underbars.append(i)
        rec(case,underbars)
        underbars.pop()

N,M = map(int,input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

flag = False
for case in permutations(S):  # case = (ab,cd,ef,gh),  최대 8!= 4* 10^4 가지
    rec(list(case),[]) 
    if flag: break

if not flag: print(-1)

