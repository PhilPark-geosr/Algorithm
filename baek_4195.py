import sys
import collections
sys.stdin = open('input_4195.txt', 'r')
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        count_dic[a] = count_dic[a] + count_dic[b]
        print(count_dic[a])
    elif a ==b:
        print(count_dic[a])
    else:
        parent[a] = b
        count_dic[b] = count_dic[b] + count_dic[a]
        print(count_dic[b])




T = int(input())
for _ in range(T):
    F = int(input())
    parent = dict()
    count_dic = collections.defaultdict(lambda : 1)
    for _ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] =b
        union(a,b)
        # print(parent, count_dic)
