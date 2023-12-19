import sys
sys.stdin = open('input_1744.txt', 'r')
input= sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num = int(input())
    num_list.append(num)

# num_list.sort()
# print(num_list)


# 양 음 구분
plus_num_list = []
minus_num_list = []
for num in num_list:
    if num >0:
        plus_num_list.append(num)
    else:
        minus_num_list.append(num)

# 정렬
plus_num_list.sort()
minus_num_list.sort(reverse= True)
    
# functionality
def check_plus_or_mul(a, b):
    if a*b >a+b:
        return True
    else:
        return False

result1 = []
while plus_num_list:
    elem = plus_num_list.pop()
    if len(plus_num_list) == 0:
        result1.append(elem)
        break
    next_elem = plus_num_list[-1]

    if check_plus_or_mul(elem, next_elem) == True:
        plus_num_list.pop()
        elem = elem*next_elem
    result1.append(elem)

result2 = []
while minus_num_list:
    elem = minus_num_list.pop()
    if len(minus_num_list) == 0:
        result2.append(elem)
        break
    next_elem = minus_num_list[-1]

    if check_plus_or_mul(elem, next_elem) == True:
        minus_num_list.pop()
        elem = elem*next_elem
    result2.append(elem)

# print(result1, result2)

answer = sum(result1) + sum(result2)
print(answer)

# print(answer)


