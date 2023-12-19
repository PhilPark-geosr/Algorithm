import sys
import itertools
sys.stdin = open('input_1062.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
# print(N)
word_list = []
for _ in range(N):
    elem = str(input())
    # print(elem)
    n = len(elem)
    # print(n, elem[4:n - 4])
    word_list.append(elem[4:n-4])

# print(word_list)
base_dic = {
    "a" : True,
    "n" : True,
    "t" : True,
    "i" : True,
    "c" : True
}
a_num = ord('a')
z_num = ord('z')
alpha_list = [chr(i) for i in range(a_num, z_num+1)]
temp = []
for alpha in alpha_list:
    if alpha not in base_dic:
        temp.append(alpha)




def make_check_dic(case):
    result_dic = base_dic.copy()
    for elem in case:
        result_dic[elem] = True
    return result_dic

def check(word):
    for w in word:
        if w not in check_dic:
            return False
    return True

if K-5 <0:
    print(0)
else:
    remain = min(K - 5, 7)
    case_list = list(itertools.combinations(temp, remain))  # 최대 7개
    answer = 0
    for case in case_list:
        # print(case)
        cnt = 0
        check_dic = make_check_dic(case)
        # print(check_dic)
        for word in word_list: #최대 50번
            if check(word) == True:
                cnt+=1

        # if cnt == 4:
        #     print(case)
        answer =max(answer, cnt)
    print(answer)


