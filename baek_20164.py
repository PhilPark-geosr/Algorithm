import sys
sys.stdin = open('input_20164.txt', 'r')
sys.setrecursionlimit(10**9)
number = input()

global max_answer
global min_answer

def get_odd_count(num:str) ->int:
    count = 0
    for elem in num:
        if int(elem) % 2 ==1:
            count +=1
    # print('count', num, count)
    return count

def combinations_with_replacement(n, r): #nHr
    r = r-n #이미 하나씩 배당해야하므로..
    if r ==0:
        return [[1 for _ in range(n)]]
    case_list = []
    def process(v, depth, check_list):
        # print(f"dfs{v, depth, check_list, r}")
        if depth == r:
            # print('check_list', check_list)
            case= []
            for i in range(len(check_list)):
                case.append(check_list[i]+1)
            case_list.append(case)
            return

        for new_idx in range(v, len(check_list)):
            check_list[new_idx] += 1
            process(new_idx, depth+1, check_list)
            check_list[new_idx] -= 1

    for i in range(n):
        check_list =[0]*n
        check_list[i] +=1
        # print('check', check_list)
        process(i, 1, check_list)

    # print('case_list', case_list)
    return case_list

# test
# print(combinations_with_replacement(3, 5))



def dfs(num, cnt):
    # print(f'dfs{num, cnt}')
    global max_answer
    global min_answer
    if len(num) ==1:
        max_answer = max(max_answer, cnt + get_odd_count(num))
        min_answer = min(min_answer, cnt + get_odd_count(num))
        return
    if len(num) ==2:
        new_cnt = cnt + get_odd_count(num)
        new_num = str(int(num[0]) + int(num[1]))
        dfs(new_num, new_cnt)
    else:
        case_list = combinations_with_replacement(3, len(num))
        # print(case_list)
        for a,b,c in case_list:
            # print(a,b,c)
            new_cnt = cnt + get_odd_count(num)
            # print(int(num[:a]) + int(num[a:a+b]) + int(num[a+b: a+b+c]))
            new_num = str(int(num[:a]) + int(num[a:a+b]) + int(num[a+b: a+b+c]) )
            dfs(new_num, new_cnt)




# cnt = get_odd_count(number)
max_answer = 0
min_answer = float('inf')
dfs(number, 0)

print(min_answer, max_answer)