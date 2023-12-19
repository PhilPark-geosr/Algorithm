import sys
import math
sys.stdin = open('input_1990.txt', 'r')
MAX_INT = 10**8
a, b =map(int, input().split())


def make_prime(a,b): #a와 b사이의 모든 소수 걸러내기
    if b > 10000000:
        b = 10000000
    is_prime = [True]*(b+1)

    # 소수 거르기
    for i in range(2, int(math.sqrt(b))+1):
        if is_prime[i] == True: #소수이면, 배수들은 모두 소수가 아니다!
            j = 2
            while j*i <= b:
                is_prime[j*i] = False
                j += 1

    # 걸러낸것들 받기
    for i in range(a, b+1):
        if is_prime[i] == True and is_pal(i) == True:
            print(i)
    print(-1)
            # result.append(i)
    # print("걸러진 소수들", result)

def is_pal(num): #소수인지 판별
    num = str(num) #일단 문자열로 변환
    if num[0] != num[-1]: #양끝다르면 그냥 종료
        return False
    else:
        n = len(num)
        for i in range(n//2):
            if num[i] != num[-i-1]:
                return False

        return True


# print(is_pal(12344321))

# --------------------- main ------------------------- #
candidates = make_prime(a,b)


