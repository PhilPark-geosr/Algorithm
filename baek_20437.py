import sys
import collections
sys.stdin = open('input_20437.txt', 'r')

input = sys.stdin.readline

ord_a = ord('a')
ord_z = ord('z')
alpha_list = list(map(chr, range(ord_a, ord_z+1)))

def check(dic, cnt):
    for elem in alpha_list:
        value = dic.get(elem, 0)
        if value == cnt:
            return True
        
    return False

def extract_min(word):
    l = 0
    r = 0
    check_dic = dict()
    answer = ""
    check_dic[word[l]] = 1
    # print('check_dic', check_dic)

    min_length = float('inf')
    while l<=r and r< n:
        # print('answer', answer)
        if check(check_dic, K) == True:
            if len(word[l:r+1]) < min_length:
                min_length= len(word[l:r+1])
                answer = word[l:r+1]
            check_dic[word[l]] -=1
            l +=1
        else:
            r +=1
            if r<n:
                value = check_dic.get(word[r], 0)
                check_dic[word[r]] = value +1
        
    return min_length

def extract_max(word):
    # 일단 모든 알파펫을 기록

    # print(char_dic)
    # 모든 키에 대해서 기록
    max_length = -1
    answer = ""
    for key in char_dic:
        arr = char_dic[key]
        if len(arr) < K:
            continue
        l = 0
        r = 0
        while l<=r and r<len(arr):
            # print('answer', answer)
            if r-l+1 > K:
                l +=1
            elif r-l +1 == K:
                if arr[r] - arr[l] +1 > max_length:
                    answer = word[arr[l]: arr[r]+1]
                    max_length = arr[r] - arr[l] +1
                r+=1
            else:
                r+=1
    return max_length

T = int(input())

for _ in range(T):
    word = input()
    K = int(input())
    n = len(word)

    char_dic = collections.defaultdict(list)
    for i, elem in enumerate(word):
        char_dic[elem].append(i)

    flag = False
    for key in char_dic:
        if len(char_dic[key]) >=K:
            flag = True
            break


    if flag == True:
        print(extract_min(word), end = " ")
        print(extract_max(word))
    else:
        print(-1)


