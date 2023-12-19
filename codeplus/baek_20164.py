import sys
import itertools
sys.setrecursionlimit(10**9)
sys.stdin = open('input_20164.txt', 'r')

number = input()

def count_odd(number):
    count=0
    for num in number:
        if int(num)%2 ==1:
            count+=1

    return count


global max_cnt
global min_cnt
def dfs(number, cnt):
    global max_cnt
    global min_cnt
    if len(number) ==1:
        cnt += count_odd(number)

        if cnt > max_cnt:
            max_cnt = cnt
        if cnt < min_cnt:
            min_cnt = cnt
        return
    
    if len(number) ==2:
        cnt += count_odd(number)
        new_number = str(int(number[0]) + int(number[1]))

        dfs(new_number, cnt)

    else:

        cnt += count_odd(number)
        n = len(number)
        temp = [i for i in range(1, n)]
        # print("temp", temp)
        caselist = itertools.combinations(temp, 2)
        for case in caselist:
            i ,j = case
            A = number[:i]
            B = number[i:j]
            C = number[j:]
            # print("A,B,C", A,B,C)
            dfs(str(int(A)+int(B)+int(C)), cnt)
           
        
max_cnt =0
min_cnt = float('inf')
dfs(number, 0)

print(min_cnt,max_cnt)