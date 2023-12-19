import sys
# sys.stdin = open('input_5904.txt', 'r')
sys.setrecursionlimit(10**9)
N = int(input())
max_num = 10**9

dp = [0]*30
dp[0] = 3
for i in range(10**5):
    dp[i] = 2*dp[i-1] + i+3
    if dp[i] >= max_num:
        # print(i)
        break
# print(dp)
section_num = -1
num = -1
for i in range(27):

    if N > dp[i]:
        continue
    elif N == dp[i]:
        section_num = i
        num = 0
        break
    else:
        section_num = i
        num = N - dp[i-1]
        break

# print(section_num, num)


def dfs(section, order):
    # print(f"dfs{section, order}")
    if section == 0:
        if order == 1:
            return 'm'
        else:
            return "o"
    if 0<= order < dp[section-1]: #첫번째 구간에 있을때
        new_order = order

        answer = dfs(section-1, new_order)
    elif dp[section-1] <= order < dp[section-1] + section +3: #두번째 구간에 있을때
        # print('여기')
        new_order = order - dp[section-1]
        if new_order == 1:
            answer = 'm'
        else:
            answer = 'o'

    else: #세번째 구간에 있을 때
        new_order = order - (dp[section-1] + section+3)
        answer = dfs(section-1, new_order)

    return answer





answer = dfs(section_num, N)
print(answer)