import sys
import heapq
import collections
import itertools
sys.setrecursionlimit(10**8)
sys.stdin = open('input_2224.txt', 'r')

N = int(input()) # 명제의 갯수

# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))

dp = [[float('inf')]*52 for _ in range(52)]
dic = dict() # 알파벳당 기록
rev_dic = dict()

upper_list = [ i for i in range(ord("A"), ord("Z")+1)] # 65 to 90
lower_list = [ i for i in range(ord("a"), ord("z")+1)] # 97 to 122

# print(upper_list)
for i in upper_list:
    dic[chr(i)] = i - 65
    rev_dic[i - 65] = chr(i)
for i in lower_list:
    dic[chr(i)] = i - 97+26
    rev_dic[i - 97+26] = chr(i)


# def convert_alpha(alpha):
#     if ord(alpha) <= 90:
#
#         return ord(alpha)-65
#     else:
#         return ord(alpha)-97 + 26


for _ in range(N):
    a, _, b = input().split()
    # print(convert_alpha(a), convert_alpha(b))
    i, j = dic[a], dic[b]
    dp[i][j] = 1

# 플로이드-와샬 수행
for k in range(52):
    for i in range(52):
        for j in range(52):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

cnt = 0 #명제 갯수
for i in range(52):
    for j in range(52):
        if dp[i][j]!=float('inf') and i!=j:
            cnt +=1
print(cnt)
# 출력
for i in range(52):
    for j in range(52):
        if dp[i][j]!=float('inf') and i!=j:
            print(f"{rev_dic[i]} => {rev_dic[j]}")
