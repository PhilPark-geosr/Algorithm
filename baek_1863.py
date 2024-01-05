import sys
sys.stdin = open('input_1863.txt', 'r')
input = sys.stdin.readline
N = int(input())
prev = 0
cur = 0

skylines = []
for _ in range(N):
    _, h = map(int, input().split())
    skylines.append(h)

answer = 0
stack = []  # 아직 건물 유지중인 애들
for h in skylines:
    # print(stack)
    if len(stack) == 0:
        stack.append(h)
        continue
    # 높이가 떨어졌을경우
    if stack[-1] > h:
        while stack:
            if stack[-1] < h:
                break
            if stack[-1] == h:
                stack.pop()
            else:
                stack.pop()
                answer += 1
    # 높이가 우상향인 경우
    stack.append(h)

# print(stack)
if stack:
    cnt = 0
    for elem in stack:
        if elem != 0:
            cnt += 1
    print(answer + cnt)
else:
    print(answer)
