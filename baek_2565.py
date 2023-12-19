import sys
sys.stdin = open('input_2565.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()
def custom_func(elem): #custom map_func
    return elem[1]

arr = list(map(custom_func, arr))
# print(arr)

dp = [1]*(N) # dp[i] : i번째까지 가장 긴 증가수열의 길이

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)

print(N- max(dp))