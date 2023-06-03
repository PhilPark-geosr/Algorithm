import sys
sys.stdin = open('input_1092.txt', 'r')

N = int(input()) # 크레인의 수
crein = list(map(int, input().split()))
M = int(input()) # 박스의 수
boxes = list(map(int, input().split()))

# 무게순으로 정렬
crein.sort() # O(NlogN)
boxes.sort() # O(MlogM)

min_crein = crein[0]
max_crein = crein[N-1]
min_box = boxes[0]
max_box = boxes[M-1]
# print(boxes)
if max_crein < max_box:
    print(-1)
else:
    time = 0
    while boxes:
        # print(boxes)
        for i in range(N-1, -1, -1):
            # print(i)
            for j in range(len(boxes)-1, -1, -1):
                # print(j)
                if boxes[j] <= crein[i]:
                    boxes.pop(j)
                    break
                
        time+=1
    print(time)