import collections
import sys
sys.stdin = open('input_14676.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
indegree = [0]*(N+1)
graph = collections.defaultdict(list)
constructed = dict() # 건설된 건물
# 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1

# ------------------ main ---------------------- #
def construct(node):
    print(f"{node} 건설")
    if indegree[node] == 0 and node not in constructed: #건설된 적 없는 애만ㄴ
        constructed[node] = True #건설되었다고 표시해주기
        for new in graph[node]:
            indegree[new] -=1 #연관된 애들 진입차수 줄여주기
        return True
    elif indegree[node] == 0 and node in constructed: #건설된 적 있는 애들은
        return True
    else: #건설할 수 없는 경우
        print('건설불가')
        return False

def destory(node):
    print(f"{node} 파괴")
    if node not in constructed: #건설된 적 없는 애들은
        return False
    constructed.pop(node, None) #건설되었던 흔적 없애기
    #진입차수 복구시키기
    for new in graph[node]:
        indegree[new] +=1

    return True

def solution():
    for _ in range(K):
        category, node = map(int, input().split())
        if category == 1:
            flag = construct(node)
        else:
            flag = destory(node)
        if flag == False:
            print("Lier!")
            return
    # 다 성공했을때
    print("King-God-Emperor")
    return
# 함수 실행
solution()

