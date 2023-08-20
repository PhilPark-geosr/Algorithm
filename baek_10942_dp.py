import sys
# sys.stdin= open('input_10942.txt', 'r')
input = sys.stdin.readline
N = int(input())
number_list = list(map(int, input().split()))
# 앞에 맞춰주기 위해 삽입
number_list.insert(0,0)
M = int(input())

# dp구하는 함수 
dp = [[-1]*(N+1) for _ in range(N+1)]
# dp initialize
for i in range(1,N+1):
    dp[i][i] = 1 #펠린드롬이다


for i in range(1, N):
    if number_list[i] == number_list[i+1]:
        dp[i][i+1] =1
    else:
        dp[i][i+1] =0
# print(dp)
# dfs정의
def dfs(i, j):
    print(f"dfs{i,j}")
    #종료조건
    # if i > j:
    #     return 1
    # 값있으면 바로 반환
    if dp[i][j]>=0:
        return dp[i][j]
    if number_list[i] != number_list[j]:
        dp[i][j] = 0
    else: #number_list[i] == number_list[j]
        if dp[i][j] == -1:
            dp[i][j] = dfs(i+1, j-1)
            # dp[i][j] =0
            # 양끝이 안같으면 펠린드롬 아니다
    
    return dp[i][j]

# for i in range(1, N+1):
#     for j in range(i+2, N+1):
#        dfs(i, j)
# for i in range(2, N):
#     for j in range(1, N-i+1):
#         dfs(j, j+i)

# 답구하기 
for _ in range(M):
    S, E = map(int, input().split())
    # print(dp[S][E])
    print(dfs(S, E))


