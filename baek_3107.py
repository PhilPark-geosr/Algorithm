import sys
sys.stdin = open('input_3107.txt', 'r')

org = input()
def pre_process(input):
    arr = []
    prev = ""
    temp = ""
    for i in range(len(input)):
        s = input[i]
        if s != ":":
            temp+=s
        else:
            if prev == ":":
                arr.append("check")
            else:
                if len(temp) >0:
                    arr.append(temp)

            temp = ""
        prev = s

    if len(temp)>0:
        arr.append(temp)
    return arr


arr = pre_process(org)
 # print(arr)

def check_colon(input):
    cnt =0
    for elem in input:
        if elem != "check":
            cnt +=1
    return cnt

def convert(elem): #0 복원
    num_of_zeros = 4 - len(elem)
    return num_of_zeros*"0" + elem

n = 8 - check_colon(arr)




result = ""
for elem in arr:
    if elem != "check":
        result += convert(elem) + ":"

    else: #elem == "check"
        result += "0000:"*n


print(result[:-1])
