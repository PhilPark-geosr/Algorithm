import sys
sys.stdin = open('input_1863.txt', 'r')
input = sys.stdin.readline
N = int(input())
prev = 0
cur = 0

cnt = 0
for _ in range(N):

    _, new = map(int, input().split())
    print(f"prev, cur, new, cnt {prev, cur, new, cnt}")
    if new == 0:
        prev = 0
        cur = 0
        continue
    if cur != new:
        # prev, cur 0일때 처리
        if prev == 0:
            cnt += 1
            cur = new
            prev = new
            continue
        if new!= prev:
            cnt +=1
            cur = new
        else: # new == prev
            cur = new

print(cnt)
