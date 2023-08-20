import sys
#sys.stdin = open('input_1931.txt', 'r')
input = sys.stdin.readline
N = int(input())
timetable = []
for _ in range(N):
    s, e = map(int, input().split())
    timetable.append((s,e))

timetable.sort(key = lambda x: (x[1], x[0]))
# print('timetable', timetable)

#끝나는 시간 = T
T = 0
cnt = 0
for s, e in timetable:
    if s>=T:
        cnt+=1
        T = e



print(cnt) 