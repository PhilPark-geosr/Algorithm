import sys
import collections
import math
sys.stdin =open('input_1669.txt', 'r')


a, b = map(int, input().split())
target = b-a #목표하고자 하는 합

def get_max_step(target):
    answer = int(math.sqrt(target))
    return answer

def get_res_cnt(res, n):
    cnt = 0
    now = n
    while res > 0:
        # print("now")
        new_res = res-now
        if new_res >=0:
            res = new_res
            cnt+=1
        else:
            now-=1
    return cnt

n = get_max_step(target)
# print(n)
res = target - n**2
# print("res", res)
m = get_res_cnt(res, n)
# print(m)

if n == 0: #바로 앞에 있는거 뽑앗을때
    print(0)
else:
    print(2*n-1 + m)
