import sys
sys.stdin = open("input_7579.txt", "r")
# input
N, M = map(int, input().split())
m_list = list(map(int, input().split())) # 메모리
c_list = list(map(int, input().split())) # 비용
m_list.insert(0,0)
c_list.insert(0,0)
sum_cost = sum(c_list)

# define dp
# dp[i][j] #1~i번째 앱을 사용하여(일부던, 전부던) j코스트로 얻을 수 있는 최대 메모리

dp = [[0]*(sum_cost+1) for _ in range(N+1)]

for i in range(1, N+1):
    # print(i)
    for j in range(sum_cost+1):
        if c_list[i] > j:
            dp[i][j] = dp[i-1][j] #i번째 앱을 재사용하는데 필요한 cost가 j를 넘으면 최대값은 1~i-1을 사용해서 만드는 메모리의 최대가 최대값임
        else:
            dp[i][j] = max(m_list[i]+ dp[i-1][j-c_list[i]], dp[i-1][j])

# 순회하면서 가장 비용이 적을때 계산
min_cost = sum_cost
for k in range(1, sum_cost+1):
    if dp[N][k] >=M: # 교체해야 하는 M의 메모리를 넘으면 업데이트
        if k < min_cost:
            min_cost = k

print(min_cost)

