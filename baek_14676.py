import collections
import sys
sys.stdin = open('input_14676.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
indegree = [0]*(N+1)
graph = collections.defaultdict(list)
constructed = collections.defaultdict(int) # 건설된 건물
# 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1

# ------------------ main ---------------------- #
def construct(node):
    # print(f"{node} 건설")
    if indegree[node] == 0: #건설할 수 있는 애들
        constructed[node] +=1 #건설카운트 +1
        if constructed[node] == 1: #건설 한개만 한 애들만 진입차수 줄여주자!
            for new in graph[node]:
                indegree[new] -= 1  # 연관된 애들 진입차수 줄여주기
        return True
    else: #건설 안되는 애들
        # print('건설불가')
        return False


def destory(node):
    # print(f"{node} 파괴")
    if constructed[node] == 0:# 건설안된 애들을 파괴하는건 잘못된 명령
        return False
    #건설된 애들
    constructed[node] -=1 #건설된 건물 하나 지우기
    if constructed[node] == 0: #이제 아예 없을 경우만 진입차수 복구시켜서 못가게 막기
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

