import sys

sys.stdin = open('input_1541.txt', 'r')
string = input()
numlist = []
stack = ""
for s in string:
    # print(s)
    if s == "-":
        numlist.append(stack)
        numlist.append(s)
        stack = ""
    else:
        stack +=s
numlist.append(stack)
# print(numlist)


# + 있는 원소 다 더해주기
for i in range(len(numlist)):
    if "+" in numlist[i]:
        templist = numlist[i].split("+")
        sum_value = 0
        for elem in templist:
            sum_value+= int(elem)
        numlist[i] = str(sum_value)

# print(numlist)
answer = int(numlist[0])
for elem in numlist[1:]:
    if elem != "-":
        answer -= int(elem)

print(answer)


