import sys 
import collections
sys.stdin = open('input_1092.txt', 'r')
# input = sys.stdin.readline

# input
N = int(input())
crein_list = list(map(int, input().split()))
M = int(input())
box_list = list(map(int, input().split()))

# 큰 순서대로 정렬
crein_list.sort(reverse=True)
box_list.sort(reverse=True)

# 예외처리
if crein_list[0] < box_list[0]:
    print(-1)
else:
    # 정답 출력
    time = 0 
    while box_list:
        for i in range(N):
            for j in range(len(box_list)):
                if crein_list[i] >= box_list[j]:
                    box_list.pop(j)
                    # if len(box_list) ==0:
                    break
        time +=1
    print(time)




