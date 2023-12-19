import sys
import heapq
sys.stdin = open('input_21939.txt', 'r')
input = sys.stdin.readline
max_heap = []
min_heap = []

remove_max_dic = dict() #제거하는 번호
remove_min_dic = dict() #제거되는 번호
def add(P,L): #번호 P, 난이도 L 추가
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))

def recommend(x):
    if x == 1:
        while True:
            p = -max_heap[0][1]
            if p not in remove_max_dic:
                print(p)
                return
            else: #문제번호가 제거대상에 있을때
                heapq.heappop(max_heap)
                remove_max_dic.pop(p, None) #지우기

    else:
        while True:
            p = min_heap[0][1]
            if p not in remove_min_dic:
                print(p)
                return
            else: #문제번호가 제거대상에 있을때
                heapq.heappop(min_heap)
                remove_min_dic.pop(p, None)  # 지우기

def solve(P):
    remove_max_dic[P] = True
    remove_min_dic[P] = True








N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    add(P,L)
M = int(input())
for _ in range(M):
    Q = input().split()
    if Q[0] == "recommend":
        x = int(Q[1])
        recommend(x)
    elif Q[0] == "add":
        P, L = int(Q[1]), int(Q[2])
        add(P,L)
    else: #Q[0] == "solve":
        P = int(Q[1])
        solve(P)
