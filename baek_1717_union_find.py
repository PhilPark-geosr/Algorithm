import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_1717.txt','r')
N, M = map(int, input().split())

parent = [i for i in range(N+1)]
# print("parent", parent)

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y #x의 부모 업데이트
        return y

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        print('YES')
    else:
        print('NO')

# main
# print("N, M", N, M)
for _ in range(M):
    category, a, b = map(int, input().split())
    # print('category, a, b', category, a, b)
    if category == 0:
        union(a, b)
    else:
        check(a,b)

