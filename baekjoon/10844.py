"""
#2차원 배열 풀이 
n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j!=0: dp[i][j] += dp[i-1][j-1]
        if j!=9: dp[i][j] += dp[i-1][j+1]

print(sum(dp[n]))
"""
#1차원 배열 풀이. 이전 계단수 다시 볼 일 없고 계산 후 버리므로, 1차원 배열로 압축 = 직전 길이인 경우 정보만 저장
n = int(input())

#길이 1일때의 계단수 개수. 0제외 모두 1개
dp = [1]*10
dp[0] = 0

for i in range(2,n+1):
    next_dp = [0]*10
    for j in range(10):
        if j!=0: next_dp[j] += dp[j-1]
        if j!=9: next_dp[j] += dp[j+1]
    dp = next_dp

print(sum(dp))
        