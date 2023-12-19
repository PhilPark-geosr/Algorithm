import sys
import math
sys.stdin = open('input_2346.txt', 'r')

GCD, LCD = map(int, input().split())
# print(math.gcd(5, 5))
def is_diff(x,y): #서로소인지 확인하는 함수
    gcd = math.gcd(x,y)
    if gcd == 1:
        return True
    return False

min_value = float('inf')
answer_x =-1
answer_y =-1
target = LCD//GCD
for x in range(1, int(math.sqrt(target))+1): ## 루트 붙여주는게 핵심이다...!
    y = target//x
    if x*y == target and is_diff(x,y) == True and x + y < min_value:
        min_value = x+y
        answer_x = x
        answer_y = y

# 정답
print(GCD*answer_x, GCD*answer_y)
