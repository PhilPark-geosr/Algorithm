import sys
sys.stdin = open('input_1439.txt', 'r')

S = input()
# 리스트로 만들기
S_list = [] #O(n)
for elem in S:
    S_list.append(elem)

# 0, 1인것들의 집합갯수
zero_cnt = 0
one_cnt = 0

temp = []
# print(S_list)
while S_list:
    elem = S_list.pop()
    if len(temp) ==0 : #비어있으면
        if elem =='0':
            zero_cnt +=1
        else:
            one_cnt +=1
        temp.append(elem)
    else: #안비어있으면 비교
        if temp[-1] != elem: #끝에것이랑 다르면..
            if elem == '0':
                zero_cnt +=1
            else:
                one_cnt +=1
            temp.pop()
            temp.append(elem)

if zero_cnt < one_cnt:
    print(zero_cnt)
else:
    print(one_cnt)
