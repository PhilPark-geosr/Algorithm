import sys
sys.stdin = open('input_2498.txt','r')

N = int(input())
arr = [0] + list(map(int, input().split()))

stack = []
for i in range(1, N+1):
    flag = False
    # print(stack)
    while stack:
        if stack[-1][0] >= arr[i]:
            print(stack[-1][1], end = " ")
            flag = True #처리 완료
            stack.append((arr[i], i))
            break
        stack.pop()
    if flag == False: #처리 안된경우
        stack.append((arr[i], i))
        print(0, end = " ")


    

