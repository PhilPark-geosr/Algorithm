import sys
sys.stdin = open("input_11054.txt", 'r')

n = int(input())
numbers = list(map(int, input().split()))
numbers.insert(0,0)

# 1 ~ i까지 가장 긴 증가수열
dp1 = [1]*(n+1)
dp1[1] = 1 #길이 1짜리
for i in range(2, n+1): #O(n^2)
    for j in range(i-1, 0, -1):
        if numbers[j] < numbers[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)
# print(dp1)

# i ~ n까지 까지 가장 긴 감소수열
dp2 = [1]*(n+1)
dp2[n] = 1 #길이 1짜리
for i in range(n-1, 0, -1): #O(n^2)
    for j in range(i+1, n+1, 1):
        if numbers[j] < numbers[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
# print(dp2)

# 바이토닉 수열
dp3 = [0]*(n+1)

for i in range(1, n+1): # O(n)
    dp3[i] = dp1[i] + dp2[i]-1

# print(dp3)

print(max(dp3))