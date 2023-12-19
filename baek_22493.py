import sys
import math
from itertools import permutations
sys.stdin = open('input_22493.txt', 'r')
K, M = map(int, input().split())

limit = 10**6
def make_prime_list(limit): #num까지의 primelist만들기
    prime_list = [True for i in range(limit +1)]
    for i in range(2, int(math.sqrt(limit)) +1):
        if prime_list[i] == True:
            j = 2
            while j*i <= limit:
                prime_list[j*i] = False
                j+=1
    return prime_list

# 소수 배열 생성
prime_list = make_prime_list(limit)

def is_prime(num):
    if prime_list[num] == True:
        return True
    return False

def cond1(num): # num = 소수 + 소수 인지(단 서로다른 소수)
    for i in range(2, num//2 +1):
        if i != num-i and is_prime(i) and is_prime(num-i):
            return True
    return False

def convert(num, M):

    while True:

        div, mod = divmod(num, M)
        if div ==0:
            break
        if mod !=0:
            break #안나눠 떨어져도
        num = num // M
    return num

def cond2(num) : # num = 소수 * 소수 인지 확인
    num = convert(num, M)
    # print('num', num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0 and is_prime(i) and is_prime(num//i):
            return True
    return False
#K 자리의 수
# cnt = 0 # 조건을 만족하는 수의 갯수
# for num in range(10**(K-1), 10**K):
#     # print('num', num)
#     if cond1(num) == True:
#         if cond2(num) == True:
#             # 이미 걸러진 애들만 검사하자!
#             cnt +=1
#
# print(cnt)

ans = 0
for num in permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], K):
    if (num[0] == '0'): continue
    num = int(''.join(num))
    if (cond1(num)):
        if (cond2(num)):
            ans += 1

print(ans)

