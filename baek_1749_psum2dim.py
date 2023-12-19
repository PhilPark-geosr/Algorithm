import sys
import itertools
sys.stdin = open('input_1749.txt', 'r')
N, M = map(int, input().split())
grid = [[0]*(M+1)]

for _ in range(N):
    line = [0] + list(map(int, input().split()))
    grid.append(line)
# print('grid', grid)

# 부분합 구해놓기
S = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + grid[i][j]

# print(S)


def get_psum(a,b,c,d):
    result = S[c][d] - S[a-1][d] - S[c][b-1] + S[a-1][b-1]
    return result



# # 모든 격자 담기
# candidates = []
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         candidates.append((i,j))
# # print("candidates", candidates)
#
# # 경우의 수 추출
# caselist = list(itertools.combinations(candidates, 2))
# print(caselist)

max_value = -float('inf')
for i in range(1, N+1):
    for j in range(1, M+1):
        # 합
        value = S[i][j]
        for k in range(1, i+1):
            for h in range(1, j+1):
                if get_psum(k,h, i, j) > max_value:
                    max_value = get_psum(k,h, i, j)

#
# for case in caselist:
#     a,b = case[0]
#     c,d = case[1]
#     # print(a, b, c,d)
#     if a <=c and b<=d:
#         p_sum = get_psum(a,b,c,d)
#         # print((a, b, c,d), p_sum)
#         if p_sum > max_value:
#             max_value = p_sum
print(max_value)

