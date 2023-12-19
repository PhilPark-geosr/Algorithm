import sys
import collections
sys.stdin = open('input_3584.txt', 'r')

def find_common_parent(N):
    
    # 공통조상 찾는 메서드
    def dfs(a,b):  # a,b의 공통조상을 찾아라
        # print(f"dfs{a,b}")
        parent_a, parent_b = parent[a], parent[b]
        if parent_a == parent_b:
            return parent_a

        else:
            new_a = dfs(parent_a, parent_b)
            return new_a

    def cal_depth(x):
        cnt = 0
        node = x
        while node >0:
            parent_node = parent[node]
            node = parent_node
            cnt +=1
        return cnt

        
    parent = [0 for _ in range(N+1)] # 부모기록


    for _ in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a

    x,y = map(int, input().split())
    # print(f"{x,y}의 공통조상을 찾아라")

    # 서로 포함관계 있는지 여부 확인
    # y가 x에 포함되니?  x contains y

    def is_contains(x, y):

        node = y
        while node >0:
            # print(node)
            parent_node = parent[node] # 부모노드 찾기
            if x == parent_node:
                return x
            else:
                node = parent_node

        return 0 # 포함하지 않으니

    if is_contains(x,y) :
        return is_contains(x,y)

    if is_contains(y,x):
        return is_contains(y,x)

    # 포함되지 않는 상황이면
    # 1. 먼저 depth를 맞춘다
    d_x, d_y = cal_depth(x), cal_depth(y)
    # print(d_x, d_y)
    if d_x < d_y: #y가 더 깊은 곳에 있으면..
        while True:
            y = parent[y]
            if cal_depth(y) == d_x:
                break
    elif d_x > d_y:
        while True:
            x = parent[x]
            if cal_depth(x) == d_y:
                break
    else: #d_x == d_y
        pass

    return dfs(x,y)











# ---------------------- main -------------------------- #
T = int(input())
for _ in range(T):
    N = int(input())
    print(find_common_parent(N))