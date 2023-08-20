import sys
import heapq
sys.stdin = open('input_1374.txt', 'r')

# input = sys.stdin.readline
# input
N = int(input())
class_list = []
for _ in range(N):
    num, s, e = map(int, input().split())
    class_list.append((num,s ,e))

class_list.sort(key = lambda x: x[1])
# print('class_list', class_list)
# 시작시간 순으로 정렬
q = [] # 강의 끝나는 시간 기록
for _, start, end in class_list:
    # print("q", q)
    # 처음에는 강의실 무조건 하나 열어야 한다
    if len(q) ==0:
        heapq.heappush(q, end)
    else:
        # 시작시간과 진행되고 있는 강의 중 가장 빨리 끝나는 시간과 비교
        # 시작시간 < 가장 빨리 끝는 시간 -> 나머지 어떤 강의실과도 같이 진행이 안됨 
        # --> 강의실 추가
        # 시간시간 >= 가장 빨리 끝나는 시간 : 이어서 할수있고, 가장 빨리 끝나는 강의실에 붙여야됨
        if start < q[0]:
            heapq.heappush(q, end)
        else:
            heapq.heappop(q)
            heapq.heappush(q, end)
    

print(len(q))

