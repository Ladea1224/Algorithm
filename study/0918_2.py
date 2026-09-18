#https://atcoder.jp/contests/adt_all_20240103_1/tasks/abc284_e


"""
.. 경로 길이 별로 나눠서 생각해봐야하나

내 경로 개수 = 1(1) + 내 연결 개수(2) + 연결의 연결 개수 (3) + 연결의 연결의 연결(4) + ...

예제2: 1+3+4+8
뭔가 직접 써보다니 순열조합 세는 느낌? 수형도 가지? 근데 이건 예제 2번 상황만 해당하나...

예제 3:
그려보니까 이거.. 수형도 항목의 개수랑 같은거네= 재귀로 전부 방문하면서 방문 할때마다+1 하면 되겠는데? 중복으로 방문 못하게 막아는 줘야하고.

근데 이거 재귀 깊이가.. 2 곱하기 10**5 이니까 파이썬 재귀제한 10**6 설정 해주면 되긴하겠다?


구현:

양방향 연결... 순서 필요없고 혹시모르니 일단 set으로..

-> 처음에 min 제약조건이랑 recursive 깊이 제한 까먹어서 오답, 
수정후 정답.

"""


import sys
sys.setrecursionlimit(10**6)

def recur(i):
    global answer
    answer+=1
    if(answer==10**6):
        print(10**6)
        exit()

    visited[i] = 1
    for x in link[i]:
        if(visited[x]): continue
        recur(x)
    visited[i] = 0


n,m = map(int,input().split())
link = [set() for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    link[u].add(v)
    link[v].add(u)

answer = 0
visited = [0]*(n+1)
recur(1)
print(answer)