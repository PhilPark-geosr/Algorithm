import sys
import collections
sys.stdin = open('input_2550.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

tree = collections.defaultdict(list)
N = int(input()) #노드 수
for _ in range(N):
    a, l, r  = map(int, input().split())
    tree[a].append((l,r))
# print(tree)

pos = collections.defaultdict(dict)
depth_dic = collections.defaultdict(list)
def dfs(v):
    # print(f"dfs{v}")
    if v == -1:
        return 0

    l_v = tree[v][0][0]
    r_v = tree[v][0][1]
    if l_v !=-1:
        left = dfs(l_v) +1
    else:
        left = dfs(l_v)
    if r_v != -1:
        right = dfs(r_v) +1
    else:
        right = dfs(r_v)
    # print("왼쪽", left,"오른쪽", right)

    if left == 0 and right ==0:
        return 0
    else:
        # print("v", v, "left", left, "right", right)
        pos[v]['left'] = left
        pos[v]['right'] = right
        return left + right
# 각자 트리 생성
dfs(1)

# print(pos)
def dfs2(v, l,r, depth):
    # print(f"dfs{v}")

    if v not in pos:
        left = 0
    else:
        left = pos[v]['left'] #왼쪽에서 얼마나 떨어져 있는지
    my_pos = l + left
    l_v = tree[v][0][0]
    r_v = tree[v][0][1]
    depth_dic[depth].append(my_pos)
    if l_v !=-1:
        dfs2(l_v, l, my_pos-1, depth+1)
    if r_v !=-1:
        dfs2(r_v, my_pos+1, r, depth+1)


dfs2(1, 1, N, 0)
# print(depth_dic)

depth_list = sorted(list(depth_dic.keys()))

answer = 0
level = -1
for depth in depth_list:
    line = depth_dic[depth]
    line.sort()
    if line[-1] - line[0]+1 > answer:
        answer =line[-1] - line[0]+1
        level = depth+1


print(level, answer)
