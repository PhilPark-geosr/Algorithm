import sys
sys.stdin = open('input_15486.txt','r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
# print(T, P)

# dp = [0]*(N+1)

# for i in range(1, N+1):

#     if i < 50:
#         if T[i] == 1:
#             for k in range(1, i):
#                 if k + T[k]-1 == i:
#                     dp[i] = max(dp[i], dp[k] + P[k]) 
#             dp[i] = max(dp[i], dp[i-1] +P[i])

#         else:
#             for k in range(1, i):
#                 if k + T[k]-1 == i:
#                     dp[i] = max(dp[i], dp[k]+P[k])

#             dp[i] = max(dp[i], dp[i-1])
#     else:
#         if T[i] == 1:
#             for k in range(i-50, i):
#                 if k + T[k]-1 == i:
#                     dp[i] = max(dp[i], dp[k] + P[k]) 
#             dp[i] = max(dp[i], dp[i-1] +P[i])

#         else:
#             for k in range(i-50, i):
#                 if k + T[k]-1 == i:
#                     dp[i] = max(dp[i], dp[k]+P[k])

#             dp[i] = max(dp[i], dp[i-1])


# for i in range(1, N+1):
#     dp[i] = max(dp[i], dp[i-1])
#     if i + T[i] -1 <=N:
        
#         dp[i + T[i] -1] = max(dp[i + T[i] -1], dp[i-1] + P[i])
dp = [0]*(N+2)
# dp[i] : i번째날 받을 수 있는 최대 수익
for i in range(1, N+1):

    if i +T[i] <= N+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
    dp[i+1] = max(dp[i+1], dp[i])

# print(dp)


print(dp[N+1])