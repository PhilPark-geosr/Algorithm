import sys

sys.stdin = open('input_18353.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
numbers.insert(0,0) # 앞에 0 삽입, 이유 : 인덱스 맞춰주기 위해서

# dp 초기화
dp =[0]*(N+1)
dp[1] =1

for i in range(2, N+1):
    #i번째 dp마다 앞에값 보면서 최신화
    max_value = 0
    for j in range(i-1, 0, -1):
        if numbers[j] > numbers[i]: #앞에 값이 큰 경우만 갱신할수 있음
            if dp[j] > max_value:
                max_value = dp[j]

    dp[i] =max_value +1

print(N- max(dp))
