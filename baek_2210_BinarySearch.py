import sys
sys.stdin =open('input_2110.txt', 'r')
input = sys.stdin.readline
N, C = map(int, input().split())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)
arr.sort()

def build(d): #d이상으로 모든 전신주 설치
    cnt =1
    standard = arr[0]
    for i in range(1, N):
        if arr[i] - standard >=d:
            cnt +=1
            standard = arr[i]
        else:
            continue
    return cnt

l = 0
r = 1e+9

answer = -1
while l<=r:
    mid = (l+r)//2
    cnt =build(mid)
    if cnt >=C:
        l = mid+1
        answer =mid
    else:
        r = mid-1

print(int(answer))