import sys
sys.stdin = open('input_20210.txt', 'r')
# input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
   elem = input()
   arr.append(elem)

# print(arr)


dic = dict()
ord_a = ord('A')
ord_z = ord('Z')
# print(ord_z - ord_a)
# print(len)
alpha = []
num = ord_a

for _ in range(26):
    alpha.append(chr(num))
    alpha.append(str.lower(chr(num)))
    num +=1
# print(alpha)

idx = -100
for elem in alpha:
    dic[elem] = idx
    idx +=1
# print(dic)

reverse_dic = dict()
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
                # result.append(str(int(temp)) + '0' * (100 - (len(temp))))
                # reverse_dic[str(int(temp)) + '0' * (100 - (len(temp)))] = temp
                result.append(str(int(temp)) + '0' * 100)
                reverse_dic[str(int(temp)) + '0' * 100 ] = temp

                # new_temp = int(temp)

                # result.append(str(new_temp).zfill(100))
                # reverse_dic[temp.zfill(100)] = temp
                temp = ""
            result.append(elem)

    if len(temp) >0:
        # result.append(str(int(temp)) + '0' * (100 - (len(temp))))
        # reverse_dic[str(int(temp)) + '0' * (100 - (len(temp)))] = temp
        result.append(str(int(temp)) + '0' * 100)
        reverse_dic[str(int(temp)) + '0' * 100] = temp
        # new_temp = int(temp)
        # result.append(str(new_temp).zfill(100))
        # reverse_dic[temp.zfill(100)] = temp
        temp = ""


    answer  = []
    for elem in result:
        if elem in dic:
            answer.append((1, dic[elem]))
            reverse_dic[str(dic[elem])] = elem
        else:
            answer.append((0, int(elem)))
    return answer

reverse_dic[""] = ""
sort_arr = []

for string in arr:
    new_string = convert(string)
    while len(new_string) < 100:
        new_string.append("")
    # print("new_string", new_string)
    # print("reverse_dic", reverse_dic)
    sort_arr.append(new_string)
sort_arr.sort()
# print(sort_arr)

# print(sort_arr)
def reverse(arr):
    result = ""
    for elem2 in arr:
        # print('elem2', elem2)
        if elem2 =="":
            continue
        result += reverse_dic[str(elem2[1])]
    return result
# sort_arr = sort_arr[::-1]

# print('sort_arr', sort_arr)
for elem3 in sort_arr:
    # print('elem3', elem3)
    org_string = reverse(elem3)
    print(org_string)


