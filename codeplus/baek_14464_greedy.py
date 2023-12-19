import sys
import heapq
sys.stdin = open('input_14464.txt', 'r')
input = sys.stdin.readline

C, N = map(int, input().split())
timelist = []
for _ in range(C):
    elem = int(input())
    timelist.append(elem)

q = []
for _ in range(N):
    start, end = map(int, input().split())
    q.append((start, end))
    # heapq.heappush(q, (end, start))

timelist.sort()
q.sort(key= lambda x:(x[1], x[0])) #빨리 끝나는 순으로

# print(q)
cnt = 0
for t in timelist:
    # print('지금시간', t)

    # 지금 시간에서 처리할수 있는 것 중 가장 끝나는 시간이 빠른거 제거
    for i in range(len(q)):
        elem = q[i]
        if elem[0] <= t<= elem[1]:
            # print("처리할 수 있는 가장 빠른 작업", elem)
            q.pop(i)
            cnt+=1
            break


print(cnt)