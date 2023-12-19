import sys
import heapq
import collections
sys.stdin = open('input_16179.txt', 'r')

input_word = input()
n = len(input_word)
check = [0]*n

def convert(arr):
    result = ""
    for i in range(n):

        if arr[i] != "0":
            result += arr[i]

    return result
def make_case(word):
    temp =[]
    for elem in word:
        temp.append(elem)
    q = []
    for i in range(n):
        # print(q)
        if check[i] == 0:
            temp[i] = input_word[i]
            # print(temp)
            new_arr = temp.copy()
            temp_word = convert(temp)
            heapq.heappush(q, (temp_word, new_arr, i))
            # print(q)
            temp[i] = "0"
    # print(q)
    return q








word = ["0" for _ in range(n)]
case_list = make_case(word)
# print(case_list[0])
while True:
    # print(f"word {word}")
    if len(convert(word)) == len(input_word):
        # print(convert(word))
        break
    else:
        case_list = make_case(word)
        # print(case_list)
        print(case_list[0][0])
        word = case_list[0][1]
        check[case_list[0][2]]=1


