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

for i in range(N):
    for j in range(N):
        sum_value = A[i] + B[j]
        sum_dic_AB[sum_value] +=1

answer = 0
for i in range(N):
    for j in range(N):
        sum_value = C[i] + D[j]
        if -sum_value in sum_dic_AB:
            answer += sum_dic_AB[-sum_value]




print(answer)
