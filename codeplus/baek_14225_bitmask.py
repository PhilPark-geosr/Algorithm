import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_14225.txt', 'r')

N = int(input())
number_list = list(map(int, input().split()))

dp = [-1]*(20*100000+1)

# 비트 연산활용
for i in range(1, (1<<N)): #모든 집합 경우의 수 탐색
    value = 0
    for j in range(N):
        if i&(1<<j): # j 번째 원소있을경우
            value += number_list[j]
    dp[value] = True
    


# main
answer = float('inf')
for i in range(1, len(dp)):
    if dp[i] ==-1:
        answer = i
        break

print(answer)




