import sys
sys.stdin = open('input_2293.txt','r')
#input=sys.stdin.readline

N, K = map(int, input().split())
money_list = []
for _ in range(N):
    money = int(input())
    money_list.append(money)
money_list.sort()
money_list.insert(0,0)
# print('money_list', money_list)

dp =[[0]*(N+1) for _ in range(K+1)]

# 값 초기화
for i in range(1, K+1):
    dp[i][1] =1

for j in range(1, N+1):
    dp[0][j] =1

# dp[1][2] =0
# dp[1][3] =0
for m in range(1, K+1):
    for i in range(1, N+1):
        # print('m, i', m, i)
        if i ==1:
            continue
        if m- money_list[i] >0:
            for k in range(i, 0, -1):
                # print("k", f"dp{m-money_list[i], k}")
                
                dp[m][i] += dp[m-money_list[i]][k]
        if m-money_list[i] ==0:
            dp[m][i] =1
        # print(f"dp{m,i}",dp[m][i])
#결과값 도출
answer = 0
for i in range(1, N+1): 
    answer += dp[K][i]

print(answer)