import sys
sys.stdin = open('input_8983.txt', 'r')
# input = sys.stdin.readline

# input
M, N, L = map(int, input().split())
shoot_list = list(map(int, input().split()))
shoot_list.sort() # 정렬
animal_list = [] # 동물의 좌표
for _ in range(N):
    a, b = map(int, input().split())
    animal_list.append([a,b])

# print('shoot_list', shoot_list)
# 가장 가까운 x좌표 찾기
def get_nearest(x, shoot_list):
    n = len(shoot_list)
    l = 0
    r = n-1

    # 가장 작은 값 찾기
    min_value = float('inf')
    result = shoot_list[0]
    while l<=r:
        
        mid = (l+r)//2
        # print('l,r', l, r, shoot_list[mid])
        if shoot_list[mid]-x ==0 : 
            return shoot_list[mid]
        if shoot_list[mid]- x > 0 :
            r = mid -1
        else:
            l = mid +1
        # 값 갱신
        if abs(shoot_list[mid]- x) < min_value:
            min_value = abs(shoot_list[mid]- x)
            result = shoot_list[mid]

    return result
        
        



# 순회하면서 사정거리 내 드는 동물 갯수 카운드
cnt = 0
for elem in animal_list:
    # y값 이미 넘어버린 애들은 바로 스킵
    x, y = elem
    if y > L:
        continue
    nearest_x = get_nearest(x, shoot_list)  # 가장 x값이 가까운 사대
    # print('nearest_x',x, nearest_x)
    distance= abs(nearest_x - x) + y
    if distance <=L:
        cnt+=1

print(cnt)
