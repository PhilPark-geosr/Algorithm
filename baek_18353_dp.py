import sys
sys.stdin = open('input_18353.txt', 'r')

N = int(input())
# 병사 리스트
soldier_list = list(map(int, input().split()))
# 인덱스 맞춰주기 위해 0 대입
soldier_list.insert(0,0)
# dp 선언
# dp[i] : soldier_list[i] 원소가 맨 끝 자리수일때, 최장 감소수열의 길이
dp = [0]*(N+1)
dp[1] = 1 # 자기자신
for i in range(2, N+1): # 최대 O(N^2)
    max_value = 0
    for k in range(i-1, 0, -1):
        if soldier_list[i] < soldier_list[k]:
            if dp[k] > max_value:
                max_value = dp[k]
    # print(max_value)
    dp[i] = max_value +1

            
print(dp)
answer = N - max(dp[1:])
print(answer)
