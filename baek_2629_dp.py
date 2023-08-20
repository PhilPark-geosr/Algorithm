import sys
# sys.stdin.readline
sys.stdin  = open('input_2629.txt', 'r')
sys.setrecursionlimit(10 ** 9)
# input
N = int(input())
weight_list = list(map(int, input().split()))
M = int(input())
ball_list = list(map(int, input().split()))
# print(weight_list)
# 이 무게 기록할 것들
dp = [[0]*40001 for _ in range(N)]
for i in range(N):
    dp[N-1][weight_list[i]] =1
# print(possible)


def dfs(v, sum_value):
    # print(f"dfs{v, sum_value}")
    if v == N:
        return 
    else:
        sum_value_list = [sum_value, sum_value+weight_list[v], abs(sum_value- weight_list[v])]
        for elem in sum_value_list:
            if dp[v][elem] ==0:
                dp[v][elem] =1
                dfs(v+1, elem)
            
dfs(0, 0)
# print(dp)


for i in range(len(ball_list)):
    if dp[N-1][ball_list[i]] ==1:
        print('Y', end = " ")
    else:
        print('N', end = " ")


