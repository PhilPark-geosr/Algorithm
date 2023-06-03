import sys
sys.stdin = open('input_14888.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
# + - x, /
operator = list(map(int, input().split()))
# print(numbers)
def solution():
    global max_result
    global min_result
    def dfs(v, result, oper):
        global max_result
        global min_result
        # print(f"dfs {v, result, numbers[v], oper}")
        if v == n-1:
            if result > max_result:
                max_result = result
            if result < min_result:
                min_result = result
        else:
            for i in range(4):
                if operator[i] != 0:
                    operator[i] -=1
                    if i == 0:
                        # print('덧셈')
                        dfs(v+1, result+numbers[v+1], oper + "+ ")
                    elif i == 1:
                        # print('뺄셈')
                        dfs(v+1, result-numbers[v+1], oper + "- ")
                    elif i == 2:
                        # print('곱셈')
                        dfs(v+1, result*numbers[v+1], oper + "* ")
                    else:
                        # print('나눗셈')
                        if result <0:
                            dfs(v+1, (-1)*(((-1)*result)//numbers[v+1]), oper + "/ ")
                        else:
                            dfs(v+1, result//numbers[v+1], oper + "/ ")
                    operator[i] +=1
                else:
                    continue
    max_result = -1e9
    min_result = 1e9
    dfs(0, numbers[0], "")
    print(max_result)
    print(min_result)

solution()