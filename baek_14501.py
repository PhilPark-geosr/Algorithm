import sys

sys.stdin = open('input_14501.txt', 'r')
n = int(input())

work = []
for i in range(1, n+1):
    time, cost = map(int, input().split())
    work.append((i, i+time-1, cost))
work.sort(key=lambda x : x[1])
print(work)

 
# initialize dp table
dp = [0]*(n+1)
for i in range(len(work)):
    result = []
    if work[i][1] == 1:
        result.append(work[i][2])
    if work[i][1] > 1:
        break
if len(result) ==0:
    dp[1] =0
else:
    dp[1] = max(result)

print(dp[1])

for i in range(3, n+1):
    에[]



