import sys
sys.stdin = open('input_1918.txt', 'r')

words = input()
priority = {
    "*" : True,
    "/" : True
}

secondary = {
    "+" : True,
    "-" : True
}
# * / 갯수 세기
cnt = 0
for elem in words:
    if elem in priority:
        cnt +=1
cnt2 = 0
for elem in words:
    if elem in secondary:
        cnt2 +=1



conv_dic = dict()
def find_priority(words):
    global num, cnt
    for i in range(len(words)):
        elem = words[i]
        if elem in priority:
            target = words[i-1] + words[i] + words[i+1]
            # print("target", target)
            convert = words[i-1] + words[i+1] + words[i]
            # print("convert", convert)

            #변환된것 기록
            conv_dic[str.lower(chr(num))] = convert
            # print(chr(num+1))
            words = words.replace(target, str.lower(chr(num)))
            # /print(words)
            cnt-=1
            num+=1
            return words

num = 97
while cnt >0:
    # print(words)
    words = find_priority(words)


def find_secondary(words):
    global num, cnt2
    for i in range(len(words)):
        elem = words[i]
        if elem in secondary:
            target = words[i - 1] + words[i] + words[i + 1]
            # print("target", target)
            convert = words[i - 1] + words[i + 1] + words[i]
            # print("convert", convert)

            # 변환된것 기록
            conv_dic[str.lower(chr(num))] = convert
            # print(chr(num + 1))
            words = words.replace(target, str.lower(chr(num)))
            # /print(words)
            cnt2 -= 1
            num += 1
            return words


while cnt2 >0:
    # print(words)
    words = find_secondary(words)


# print(conv_dic)
#다 처리 되고 남은 애들
# print(words)
temp = conv_dic[words]
# print(temp)


while True:
    flag = False
    for elem in temp:
        # print("elem", elem)
        if elem in conv_dic:
            # print(conv_dic[elem])
            temp = temp.replace(elem, conv_dic[elem])
            flag = True
            # print(temp)
            break
    if flag == False:
        break

print(temp)

#
# print(ord("a"))