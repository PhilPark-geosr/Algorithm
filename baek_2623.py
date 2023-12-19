import sys
import collections
sys.stdin = open('input_2623.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())

indegree = [0]*(N+1) #진입차수
graph = collections.defaultdict(list)
# 초기 세팅
def make_relation(arr):
    node = arr[0]
    for v in arr[1:]:
        graph[node].append(v) #그래프 연결관계 생성
        indegree[v] +=1
        node = v

def topology_sort():
    q = collections.deque()
    # 진입차수 0인애들 넣기
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    answer = []
    while q:
        # print("q", q)
        now = q.popleft()
        answer.append(now) #경로에 추가
        for node in graph[now]:
            indegree[node] -=1
            if indegree[node] ==0:
                q.append(node)
    return answer

# 초기 세팅
for _ in range(M):
    elem = list(map(int, input().split()))
    num, relation = elem[0], elem[1:]
    make_relation(relation)

# print(graph)
# print(indegree)

# 위상정렬 수행
result = topology_sort()
if len(result) < N: # 출력이 불가능한 경우
    print(0)
else:
    #결과 출력
    for elem in result:
        print(elem)