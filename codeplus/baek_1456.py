import sys
import math
sys.stdin = open('input_1456.txt', 'r')
# input = sys.stdin.readline
start, end = map(int, input().split())
# start, end = int(math.sqrt(start)), int(math.sqrt(end))
# print(start, end)

MAX_NUM = 10**14

def get_prime_number_list(n):
    check = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if check[i] == True:
            j = 2
            while j*i <=n:   
                check[i*j] = False      
                j+=1
                    
    # print(check)
    return check

check_list = get_prime_number_list(int(math.sqrt(end)))

cnt = 0
for i in range(2, int(math.sqrt(end))+1):
    # print('i', i)
    num = check_list[i]
    # print('num', num)
    if num == True:
        value = i
        k = 2
        while value**k <= end:
            if start<=value**k<=end :
                cnt+=1
            k+=1


print(cnt)