#https://atcoder.jp/contests/adt_all_20240103_1/tasks/abc284_e

#시간 복잡도 - dfs방문 * 반복문 = 10**6 * 10 = 10**7 
#제한 없을 시 N! (수형도 그려지는 느낌이므로.. 참고로 10! = 10^6~10^7이라 N이 10정도 까지는 가능함. )
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