import sys
# sys.stdin.readline
sys.stdin  = open('input_2629.txt', 'r')
sys.setrecursionlimit(10 ** 9)
# input
N = int(input())
weight_list = list(map(int, input().split()))
M = int(input())
ball_list = list(map(int, input().split()))

# 이 무게 기록할 것들
dic = dict()
possible = set()
for i in range(N):
    dic[weight_list[i]] = True
    possible.add(weight_list[i])
possible.add(0)
# print(possible)


def dfs(v, sum_value):
    # print(f"dfs{v, sum_value}")
    if v == N-1:
        return 
    else:
        if abs(sum_value-weight_list[v+1]) not in dic:
            dfs(v+1, sum_value-weight_list[v+1])
            dic[abs(sum_value-weight_list[v+1])] =True
            possible.add(abs(sum_value-weight_list[v+1]))
        if abs(sum_value+weight_list[v+1]) not in dic:
            dfs(v+1, sum_value+weight_list[v+1])
            dic[abs(sum_value+weight_list[v+1])] =True
            possible.add(abs(sum_value+weight_list[v+1]))
        
        dfs(v+1, sum_value)
        # dic[abs(sum_value)] =True
        possible.add(sum_value)
dfs(0, weight_list[0])
# print(possible)


for i in range(len(ball_list)):
    if ball_list[i] in possible:
        print('Y', end = " ")
    else:
        print('N', end = " ")
# global flag
# def dfs(v, sum_value, target):
#     print(f"dfs{v, sum_value, target, dic}")
#     global flag
#     if v == N-1:
#         return
#     if sum_value == target:
#         flag = True
#     else:
#         # dic에 없을때만 수행
#         if abs(sum_value-weight_list[v+1]) not in dic:
#             dfs(v+1, abs(sum_value-weight_list[v+1]), target)
#             dic[abs(sum_value-weight_list[v+1])] =True
#         if abs(sum_value+weight_list[v+1]) not in dic:
#             dfs(v+1, abs(sum_value+weight_list[v+1]), target)
#             dic[abs(sum_value+weight_list[v+1])] =True
# print(ball_list)
# 답 구하기
# for i in range(len(ball_list)):
#     flag = False
#     dfs(0, weight_list[0], ball_list[i])
#     if flag ==True:
#         print('Y')
#     else:
#         print('N')

