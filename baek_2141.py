import sys
sys.stdin = open('input_2141.txt', 'r')
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    x, a = map(int, input().split())
    arr.append((x,a))

arr.sort(key = lambda x : x[0])
# print(arr)
p_sum = [0]*(N+1)
for i in range(1, N+1):
    p_sum[i] = p_sum[i-1] + arr[i-1][1]

# print(p_sum)

for i in range(1, N+1):
    # print(p_sum[i], p_sum[N] - p_sum[i])
    if p_sum[i] >= p_sum[N] - p_sum[i]:
        print(arr[i-1][0])
        break
