import sys
import collections
sys.stdin = open('input_1669.txt', 'r')
monkey, dog = map(int, input().split())

def make_up_list(up):
    if up ==0:
        return [1]
    else:
        return [up-1, up, up+1]

def bfs(monkey, dog):
    q = collections.deque()
    q.append((monkey, 0, 0))

    while q:
        height, up, day = q.popleft()
        print(height, up, day)
        if height == dog and up == 1:
            return day
        uplist = make_up_list(up)
        print(uplist)
        for new_up in uplist:
            new_height = height + new_up
            q.append((new_height, new_up, day+1))








# ----------------------- main ------------------------------- #
answer = bfs(monkey,dog)
print(answer)

