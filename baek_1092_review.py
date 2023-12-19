import sys
sys.stdin = open('input_1092.txt', 'r')
input = sys.stdin.readline
N = int(input())
creins = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))


# 정렬
creins.sort(reverse =True)
boxes.sort(reverse = True)

# print(creins, boxes)
def solution():
    def remove_box(w):
        for elem in boxes:
            if w>=elem:
                boxes.remove(elem)
                # print(f"{elem}가 {w}를 만나 제거 됩니다")
                return 1
        return 0
    t=0
    while boxes:
        cnt = 0
        for w in creins:
            cnt += remove_box(w)
        if cnt == 0: # 하나라도 제거를 못하는 상황이 나올 경우..
            print(-1)
            return
        t+=1


    print(t)

solution()