import sys
import collections
sys.stdin = open('input_16562.txt', 'r')
input = sys.stdin.readline
N, M, K  = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parents = [i for i in range(N+1)]

def find(x):
    if parents[x] ==x:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b




# union 수행
for _ in range(M):
    a, b = map(int, input().split())
    union(a,b)
# print(parents)

# 모든 노드에 대해 다시 부모를 찾아준다 --> 핵심 포인트 였다!!!!!!
for i in range(1, N+1):
    find(i)

# 딕셔너리 만들기
dic = collections.defaultdict(list)
for i in range(1, N+1):
    dic[parents[i]].append(i)

# print("dic", dic)

def find_min(arr):
    min_value = 10000
    for elem in arr:
        min_value = min(min_value, cost[elem])
    return min_value


answer = 0
for key in dic:
    idx_list = dic[key]
    min_value = find_min(idx_list)
    answer += min_value

#정답 추출

if answer <=K:
    print(answer)
else:
    print('Oh no')


