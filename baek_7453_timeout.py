import sys
import collections
sys.stdin = open('input_7453.txt', 'r')
input = sys.stdin.readline
N = int(input())
A = []
B = []
C = []
D = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# print(A,B,C,D)

sum_dic_AB = collections.defaultdict(int)
sum_dic_CD = collections.defaultdict(int)


def dfs(category, v, sum_value):
    if category == "A":

        for i in range(N):
            dfs("B", i, sum_value + B[i])
        return

    # if category == "C":
    #
    #     for i in range(N):
    #         dfs("D", i, sum_value + D[i])
    #     return

    if category == "B":
        sum_dic_AB[sum_value] +=1
        return
    # if category == "D":
    #     sum_dic_CD[sum_value] += 1
    #     return

def dfs2(category, v, sum_value):
    # if category == "A":
    #
    #     for i in range(N):
    #         dfs("B", i, sum_value + B[i])
    #     return

    if category == "C":

        for i in range(N):
            dfs2("D", i, sum_value + D[i])
        return

    # if category == "B":
    #     sum_dic_AB[sum_value] +=1
    #     return
    if category == "D":
        sum_dic_CD[sum_value] += 1
        return


# AB 합의 집합구하기
for i in range(N):
    dfs("A", i, A[i])


for i in range(N):
    dfs2("C", i, C[i])

# print(sum_dic_AB)
# print(sum_dic_CD)

answer = 0
for key in sum_dic_AB:

    if -key in sum_dic_CD:

        cnt = sum_dic_AB[key]*sum_dic_CD[-key]
        # print("key", key, "cnt", cnt)
        answer +=cnt

print(answer)
