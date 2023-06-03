import sys
sys.stdin = open('input_21758.txt', 'r')

n = int(input())
honey_list = list(map(int, input().split()))

# 부분합 만들기
# dp[i] # i번째원소까지의 합
dp = [0]*n
dp[0] = honey_list[0]
for i in range(1,n):
    dp[i] = dp[i-1]+ honey_list[i]
# print(dp)

## sl + al 최솟값 찾기
min_value_case1 = float('inf')
for k in range(1, n-1):
    if dp[k]+ honey_list[k] < min_value_case1:
        min_value_case1 = dp[k]+ honey_list[k] #업데이트
min_value_case1 = 2*dp[n-1] -dp[0] - min_value_case1

# min_value_case2
min_value_case2 = float('inf')
for h in range(1, n-1):
    # print(honey_list[h])
    if honey_list[h] < min_value_case2:
        min_value_case2 = honey_list[h] 
# print(min_value_case2)
min_value_case2 = min_value_case2 + dp[n-2] - dp[0]


# min_value_case3
max_value_case3 = 0
for j in range(1, n-1):
    if dp[j-1] - honey_list[j] > max_value_case3:
        max_value_case3 = dp[j-1] - honey_list[j]
max_value_case3 = max_value_case3 + dp[n-2]
# print(min_value_case1, min_value_case2, max_value_case3)

answer = max(min_value_case1, min_value_case2, max_value_case3)
print(answer)