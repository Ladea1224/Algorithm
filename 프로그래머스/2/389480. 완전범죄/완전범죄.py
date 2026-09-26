"""
똑같은 순번에서 똑같은 결과에 도달했다면, 도달한 방법과 무관하게 이후 진행 과정은 동일하다.
따라서 특정 순번에서 특정 결과에 도달 가능한지 여부를 배열에 저장한다.

"""
#1.3차원 DP[i][a][b] = i번째 순번에서 a,b 에 도달 가능한지 여부
def solution(info, n, m):
    infoCnt = len(info)
    dp = [[[False]*m for _ in range(n)] for _ in range(infoCnt+1)]
    dp[0][0][0] = True
    
    for i in range(infoCnt):
        A,B = info[i]
        for a in range(n):
            for b in range(m):
                if not dp[i][a][b]: continue
                
                if a+A < n:
                    dp[i+1][a+A][b] = True
                if b+B < m:
                    dp[i+1][a][b+B] = True
    
    return next( (a for a in range(n) for b in range(m) if dp[infoCnt][a][b]),-1)

# #DFS 로 구현
# def solution(info, n, m):
#     infoCnt = len(info)

#     # dp[i][a][b]
#     # = 앞의 i개 물건을 처리해서 (a, b)에 도달했는가?
#     dp = [[[False] * m for _ in range(n)]
#           for _ in range(infoCnt + 1)]

#     def dfs(i, a, b):
#         # 이미 방문한 상태라면 다시 계산하지 않음
#         if dp[i][a][b]:
#             return

#         dp[i][a][b] = True

#         # 모든 물건 처리
#         if i == infoCnt:
#             return

#         A, B = info[i]

#         # A가 훔침
#         if a + A < n:
#             dfs(i + 1, a + A, b)

#         # B가 훔침
#         if b + B < m:
#             dfs(i + 1, a, b + B)

#     dfs(0, 0, 0)

#     return next(
#         (a for a in range(n)
#          for b in range(m)
#          if dp[infoCnt][a][b]),
#         -1
#     )

#BFS로 구현
# from collections import deque
# def solution(info, n, m):
#     infoCnt = len(info)

#     # dp[i][a][b]
#     # = 앞의 i개 물건을 처리해서
#     #   A 흔적이 a, B 흔적이 b인 상태가 가능한가?
#     dp = [[[False] * m for _ in range(n)]
#           for _ in range(infoCnt + 1)]

#     q = deque()

#     # 시작 상태
#     dp[0][0][0] = True
#     q.append((0, 0, 0))

#     while q:
#         i, a, b = q.popleft()

#         # 모든 물건을 처리했다면 더 이상 전파할 필요 없음
#         if i == infoCnt:
#             continue

#         A, B = info[i]

#         # A가 훔치는 경우
#         na = a + A
#         if na < n and not dp[i + 1][na][b]:
#             dp[i + 1][na][b] = True
#             q.append((i + 1, na, b))

#         # B가 훔치는 경우
#         nb = b + B
#         if nb < m and not dp[i + 1][a][nb]:
#             dp[i + 1][a][nb] = True
#             q.append((i + 1, a, nb))

#     # 모든 물건을 처리한 뒤 A 흔적의 최소값
#     return next(
#         (a for a in range(n)
#          for b in range(m)
#          if dp[infoCnt][a][b]),
#         -1
#     )


#2.2차원 DP. i 상태가 이후에 필요하지 않으므로. dp[a][b] = "현재까지" 처리한 물건으로 (a,b)가 가능한가?
# def solution(info, n, m):
#     # dp[a][b] = 현재까지 처리한 물건으로
#     #            A 흔적 a, B 흔적 b가 가능한가?
#     dp = [[False] * m for _ in range(n)]

#     dp[0][0] = True

#     for A, B in info:
#         next_dp = [[False] * m for _ in range(n)]

#         for a in range(n):
#             for b in range(m):
#                 if not dp[a][b]:
#                     continue

#                 # A가 훔침
#                 if a + A < n:
#                     next_dp[a + A][b] = True

#                 # B가 훔침
#                 if b + B < m:
#                     next_dp[a][b + B] = True

#         dp = next_dp

#     # 가능한 상태 중 A 흔적의 최소값
#     return next(
#         (a for a in range(n)
#          for b in range(m)
#          if dp[a][b]),
#         -1
#     )

#(예정)
#3.1차원 DP dp[b] = B의 흔적이 정확히 b일 때,가능한 A의 흔적의 최솟값.
#겹치지 않도록 임시 dp를 만들거나 ,역순으로 채워나가야 한다.

    
