import sys
from bisect import bisect_left
sys.stdin = open('input_8983.txt', 'r')

M, N, L = map(int, input().split()) # M : 사대의 수, N : 동물의 수, L : 사정거리

# 사대위치
shoot_list = list(map(int, input().split()))
shoot_list.sort() # 좌표 순으로 정렬  O(mlogm)

# 동물 좌표 
animal_list = []
for _ in range(N):
    a, b = map(int, input().split())
    animal_list.append((a,b))

# animal_list.sort(key = lambda x : x[0]) #x좌표 가까운 순으로 정렬 , O(nlogn)

# print(shoot_list)
# 각각 확인

# functionality
def nearlist_idx(arr:list, target:int) -> int:
    n = len(arr)
    l = 0
    r = n-1
    min_dis = float('inf') #최소거리 갱신
    answer = 0
    while l<=r:
        # print(l, r)
        
        mid = (l+r)//2
        if abs(target-arr[mid]) < min_dis:
            min_dis = abs(target-arr[mid])
            answer = mid
            if target-arr[mid] >0:
                l = mid +1
            elif target-arr[mid] ==0 : 
                break #이게 제일 최소거리
            else:
                r = mid -1
        else:
            if target-arr[mid] >0:
                l = mid +1
            else:
                r = mid -1
    return answer


count = 0 #잡을 수 있는 동물의 수 
for (x, y) in animal_list:
    # print('x', x)
    if y > L: # 이미 사정거리 넘어가는 경우 불가
        continue
    else:
        # 가장 가까운 사대 찾기
        idx = nearlist_idx(shoot_list, x)
        # print('idx',idx)
        dist = abs(x - shoot_list[idx]) + y
        if dist <= L:
            count+=1

print(count)