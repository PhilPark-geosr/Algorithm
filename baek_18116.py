import sys
import collections
sys.stdin = open('input_18116.txt', 'r')
input = sys.stdin.readline

parent = [i for i in range(10**6+1)]
cnt = [1 for _ in range(10**6+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a<b:
        parent[b] = a
        cnt[a] += cnt[b]
    else:
        parent[a] =b
        cnt[b] += cnt[a]


N = int(input())

for _ in range(N):
    Q = input().split()
    # print("Q", Q)
    if Q[0] == 'I':
        a, b = int(Q[1]), int(Q[2])
        union(a,b)


    else: #Q[0] == "Q"
        a = int(Q[1])
        print(cnt[find(a)])

