import sys
sys.stdin = open('input_1912.txt', 'r')
n = int(input())
numbers = list(map(int, input().split()))
# print(numbers)

# sol1 : 시간초과
# dp 구간합 만들기
# dp[i] : 0~i까지 합
# dp = [0]*(n+1)
# for i in range(1, n+1):
#     dp[i] = dp[i-1] + numbers[i-1]
# # print(dp)

# # 가장 큰 구간합 구하기

# max_value = max(dp)
# min_value = min(dp)
# # print(max_value, min_value)

# # 구간합 구하기
# answer =0
# for i in range(1, n):
#     for j in range(i+1, n+1):
#         temp = dp[j] - dp[i]
#         if temp > answer:
#             answer = temp

# if answer > max_value:
#     print(answer)
# else:
#     print(max_value)    


# sol2
# dp : i번째가 마지막항으로하는 연속된수열의 합
dp = [0]*(n+1)
dp[0] =0
#initialize dp
for i in range(1, n+1):
    dp[i] = numbers[i-1]
print(numbers)
for i in range(1, n+1):
    dp[i] = max(dp[i-1]+ numbers[i-1], numbers[i-1])

print(max(dp))