import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_13392.txt', 'r')
input = sys.stdin.readline

N = int(input())
base = input()
target = input()
base = '0'+base +'00'
target = '0' + target +'00'

# print('base, target', base, target)

dp = [[float('inf')]*10 for _ in range(N+1)]

def dfs(i, left, total_cost):
    # print(f"dfs{i,left, total_cost}")
    if i == N+1:
        return
    if dp[i][left] <=total_cost:
        print('이미 기록된 값이 있습니다..')
        return
    # 최소갱신
    dp[i][left] = total_cost
    if i+1 <=N:
    # 맞춰야 될 번호 구하기
        cur = (int(base[i+1]) + left) % 10
        # print('현재 번호, 맞춰야 되는 번호', cur, target[i+1])
        left_cost = (int(target[i+1])- cur +10)%10 #왼쪽으로 회전 할 경우 발생하는 cost
        right_cost = (cur-int(target[i+1]) +10)%10 #오른쪽으로 회전 할 경우 발생하는 cost

        # 왼쪽회전
        dfs(i+1, (left+ left_cost)%10, total_cost+ left_cost)
        # 오른쪽 회전
        dfs(i + 1, left, total_cost + right_cost)
    # dfs(i+1, (left + (int(target[i])-cur +10)%10)%10, right)
    # dfs(i+1, left, right+(cur-int(target[i]) +10)%10)

dfs(0, 0, 0)
print(dp)
print(min(dp[N]))