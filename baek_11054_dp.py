import sys
sys.stdin = open('input_11054.txt', 'r')

N = int(input())
numberlist = list(map(int, input().split()))
reversed_numberlist= numberlist[::-1]
# print(numberlist)
# print(reversed_numberlist)
#dp initialize 
# dp[i] i번째 항이 끝항인 최대 증가수열의 길이

dp1 = [0]*(N+1)
dp2 = [0]*(N+1)
for i in range(1, N+1):
    max_value = 0
    for k in range(i-1, -1, -1): 
        if numberlist[k-1] < numberlist[i-1]: 
            max_value = max(dp1[k], max_value)
    dp1[i] = max_value +1

# print(dp1)
for i in range(1, N+1):
    max_value = 0
    for k in range(i-1, -1, -1): 
        if reversed_numberlist[k-1] < reversed_numberlist[i-1]: 
            max_value = max(dp2[k], max_value)
    dp2[i] = max_value +1
# print(dp2)

# 정답 계산
answer = 0
for j in range(1, N+1):
    answer = max(dp1[j] + dp2[-j], answer)

print(answer-1)




