n,m = map(int, input().split())
tp = ["00"]+[input() for _ in range(n)]

dp = [1e9]*(n+1)
dp[1] = 1
for i in range(1,n):
    for j in range(m):
        if tp[i][j]=="0": continue
        idx = i+1+j
        dp[idx] = min(dp[idx],dp[i]+1)
print(*dp)




        