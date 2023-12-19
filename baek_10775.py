import sys
import collections
sys.stdin = open('input_10775.txt', 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

G = int(input())
P = int(input())

visited = [0 for _ in range(G+1)]
visited[0] = 1

next_dic = [0 for _ in range(G+1)]
# initialize
for i in range(1, G+1):
    next_dic[i] = i

global flag


global check
check= 0
def dfs(v: int, path: list) -> None:
    global flag
    # global check
    # check+=1
    # if check <=12:
    #     print(f"dfs{v, next_dic, path}")

    if v == 0:
        flag = False
        return
    if visited[v] == 0:
        visited[v] = 1
        #update
        for elem in path:
            next_dic[elem] = v-1
        return

    else:
        next_v = next_dic[v]
        dfs(next_v, path + [next_v])




# --------------------------- main ------------------------------------ #
cnt = 0
for _ in range(P):
    # print(visited)
    a = int(input())
    flag = True
    dfs(a, [a])
    if flag == False:
        break
    cnt+=1


print(cnt)