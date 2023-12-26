import sys
sys.stdin = open('input_1863.txt', 'r')
input = sys.stdin.readline
N = int(input())
prev = 0
cur = 0

cnt = 0
for _ in range(N):

    _, new = map(int, input().split())
    #print(f"prev, cur, new, cnt {prev, cur, new, cnt}")
    if new == 0:
        prev = 0
        cur = 0
        continue
    
    # 처음 들어왔을때 처리
    if prev == 0:
        cnt += 1
        cur = new
        prev = new
        continue
        
    # 나머지 처리
    if prev < cur:
        if new > cur:
            cnt +=1
            cur = new

        elif new == cur:
            pass
        else: #new < cur
            if new < prev:
                cnt +=1
                prev = cur
                cur = new
            elif new == prev:
                cur = new
            else:
                cnt+=1
                cur = new

    elif prev == cur:
        if new > cur:
            cnt +=1
            cur = new


        elif new == cur:
            pass

        else: #new < cur
            cnt +=1
            cur = new

    else: #prev > cur
        if new > cur:
            cnt +=1
            prev = cur
            cur = new
        elif new == cur:
            cnt += 1
            prev = cur
            cur = new

        else: #new < cur
            cnt+=1
            prev = cur
            cur = new





print(cnt)
