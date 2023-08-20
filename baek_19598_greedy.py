import sys
# input = sys.stdin.readline 
sys.stdin = open('input_19598.txt', 'r')
import heapq

# input
N = int(input())

# 끝나는 순으로 정렬
q = []
for _ in range(N):
    S, E = map(int, input().split())
    heapq.heappush(q, (S, E)) #시작 순으로     

work_q = [] #열려있는 회의실

# q에 넣고 비교
while q:
    # print(q, work_q)
    if len(work_q) ==0: #처음 비어있을때 그냥 넣는다
        S,E = heapq.heappop(q)
        heapq.heappush(work_q, E)
    else:
        # work_q = [30, 50] 
        # 회의실 두개 열려있음.. 젤 빨리 끝나는 곳보다 시작시간이 빠르면 아무데서도 회의 진해을 못하므로, 회의실 하나 더 개설
        S,E = heapq.heappop(q) # 남은것중 가장 빨리 끝나는 거 뽑아서.. 
        if S < work_q[0]:
            heapq.heappush(work_q, E)
        else:
            # 다음 회의시작시간 교체
            heapq.heappop(work_q)
            heapq.heappush(work_q, E)

# print(work_q)


# 답
print(len(work_q))