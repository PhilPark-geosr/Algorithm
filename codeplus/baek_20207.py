import sys
sys.stdin = open('input_20207.txt', 'r')
input = sys.stdin.readline

N = int(input())
p_sum = [0]*367

for _ in range(N):
    S, E = map(int, input().split())
    p_sum[S] +=1
    p_sum[E+1] -=1

# print(p_sum)

for i in range(1, 367):
    p_sum[i] +=p_sum[i-1]

# print(p_sum)

max_height = 0
cnt = 0
answer = 0
for i in range(1, 367):
    if p_sum[i] >=1:
        max_height = max(max_height, p_sum[i])
        cnt+=1
    else:
        answer += max_height*cnt
        cnt=0
        max_height = 0

print(answer)

