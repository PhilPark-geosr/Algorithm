import sys
sys.stdin = open('input_1174.txt', 'r')
sys.setrecursionlimit(10**9)
N = int(input())



result = []
def dfs(number:str) -> None:
    
    # print(f"dfs{number}")
    if number == "":
        for i in range(10):
            dfs(str(i))
    else:
        result.append(int(number))
        for i in range(10):
            if i > int(number[0]):
                dfs(str(i)+number)




dfs("")
# print(len(result))

# 정답 도출
if N > len(result):
    print(-1)
else:
    result.sort()
    print(result[N-1])