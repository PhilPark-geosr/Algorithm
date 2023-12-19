import sys
sys.stdin = open('input_14002.txt', 'r')
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [1]*(N+1)
path = [-1]*(N+1)
dp[0] =0

for i in range(2, N+1):
    for j in range(1, i):
        if numbers[i] > numbers[j]:
            if dp[j] +1 > dp[i]:
                dp[i] = dp[j] +1
                path[i] = j
#
# print(dp)
# print(path)

# 최대 길이
max_value = max(dp)
# 최대 길이를 출력하는 idx
last_idx = dp.index(max_value)

answer = [] #경로
node = last_idx
while node > 0:
    answer.append(node)
    node = path[node]

# print(answer)


# 결과 출력
print(max_value) # 최장 수열 길이
# 최장수열
for i in range(len(answer)-1, -1, -1):
    print(numbers[answer[i]], end =" ")

