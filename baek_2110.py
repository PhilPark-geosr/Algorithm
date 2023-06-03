import sys
sys.stdin = open("input_2110.txt", 'r')

N, C = map(int, input().split())
# make numbers
numbers = [] #O(N)
for _ in range(N):
    a = int(input())
    numbers.append(a)

# sort numbers O(nlogn)
numbers.sort()

# 공유기 배치 함수
def set_wifi(array, dis):
    n = len(array)
    count = 1
    # 포인터 정의
    cur = 0
    next = 1
    while next < n:
        if numbers[next] - numbers[cur] >= dis:
            count+=1
            cur = next
            next = cur+1
        else:
            next +=1
    return count

# 최대거리 찾기

l = 1
r = numbers[N-1]
answer =0
while l<=r:
    mid =(l+r)//2
    if set_wifi(numbers, mid) >=C:
        l = mid +1
        answer =mid
    else:
        r = mid -1

print(answer)


