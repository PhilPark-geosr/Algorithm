import sys
sys.stdin = open('Q_41_input.txt','r')
N, M = map(int, input().split())

graph =  [[0]*(N+1)]

#find - union
def find(parent, x):
    if parent[x] !=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] =a
    else:
        parent[a] =b

# parent table
parent = [i for i in range(N+1)]
print(parent)
#make a graph
for _ in range(N):
    line = [0] + list(map(int, input().split()))
    graph.append(line)
print(graph)
# do union
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] ==1:
            union(parent, i,j)

travel_list =  list(map(int, input().split()))

#확인
confirm =[]
standard = find(parent, travel_list[0])
flag = True
for k in range(1, len(travel_list)):
    temp = find(parent, travel_list[k])
    confirm.append(temp)
    if standard != temp:
        flag = False
        break
print(confirm)
if flag == True:
    print('YES')
else:
    print('NO')


'''
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
'''
