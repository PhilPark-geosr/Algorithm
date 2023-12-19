import sys
from functools import cmp_to_key
sys.stdin = open('input_20210.txt', 'r')
# input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    elem = input()
    arr.append(elem)

def convert(string):

    result = []
    temp = ""
    temp2 = ""
    for i in range(len(string)):
        elem = string[i]
        # print(elem, temp)
        if elem in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            temp += elem
        else:
            if len(temp) >0:
                result.append(temp)
                temp = ""
            result.append(elem)

    if len(temp) >0:
        result.append(temp)
        temp = ""

    return result

def compare(A, B): # A, B배열 비교
    n= min(len(A), len(B))
    for i in range(n):
        if A[i] == B[i]: # 두 값이 같으면 그냥 스킵
            continue
        if A[i].isdigit() == True and B[i].isdigit() == False: #숫자 vs 문자 -> 숫자
            return -1
        if A[i].isdigit() == False and B[i].isdigit() == True: #문자 vs 숫자 -> 숫자
            return 1
        if A[i].isdigit() == False and B[i].isdigit() == False: #둘다 문자
            if A[i].lower() == B[i].lower(): #둘다 문자가 같을때
                if A[i].islower() == False: # A가 대문자일경우
                    return -1
                else:
                    return 1
            else:
                if A[i].lower() < B[i].lower():
                    return -1
                else:
                    return 1
        # 둘다 숫자일 경우
        if int(A[i]) == int(B[i]): #숫자가 같을경우
            if len(A[i]) < len(B[i]): # 0 갯수가 적은게 앞에 온다
                return -1
            else:
                return 1
        else:
            if int(A[i]) < int(B[i]):
                return -1
            else:
                return 1
    if len(A) < len(B):
        return -1
    else:
        return 1

# 문자열 변환하기
sort_arr = []
for string in arr:
    new_string = convert(string)
    # print("new_string", new_string)
    sort_arr.append(new_string)

# 문자열 정렬하기
sort_arr.sort(key = cmp_to_key(compare))

# 정답 출력하기
for elem in sort_arr:
    print("".join(elem))


