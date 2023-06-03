import sys
sys.stdin = open('input_10942.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
numbers.insert(0,0)

m  = int(input())
q_list= []
for _ in range(m):
    s, e = map(int, input().split())
    q_list.append((s,e))

# dp[i][j] numbers의 i ~ j까지 펠린드롬 여부
# dp initialize
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] =1

for j in range(1, n):
    if numbers[j] == numbers[j+1]:
        dp[j][j+1] = 1

# dp 계산
for i in range(2, n):
    for j in range(1, n-i +1):
        if numbers[j] == numbers[j+i]:
            dp[j][j+i] = dp[j+1][j+i-1]
# 판별
for q in q_list:
    a, b = q
    print(dp[a][b])


