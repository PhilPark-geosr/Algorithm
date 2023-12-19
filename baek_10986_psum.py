import collections
import sys
sys.stdin = open('input_10986.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 구간합 구해놓기
p_sum = [0]*(N+1)
for i in range(1, N+1):
    p_sum[i] = p_sum[i-1] + numbers[i-1]
    p_sum[i] %= M

#print('p_sum', p_sum)

# 기록테이블 구성
dic = collections.defaultdict(int)
dic[0] =1
# M으로 나눠떨어지는 구간 계산하기
cnt = 0
for i in range(1, N+1):

    target = p_sum[i]
    cnt+=dic[target]
    dic[target]+=1

print(cnt)



