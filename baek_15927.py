import sys
sys.stdin = open('input_15927.txt', 'r')
sys.setrecursionlimit(10**9)

word = input()
N = len(word)

def is_palindrome(word, l, r):
    if l >=r: #넘어가면
        return True
    if word[l] == word[r]:# 펠린드롬 후보
        check = is_palindrome(word, l+1, r-1)
        if check == True:
            return True
        else:
            return False
    else:
        return False



word_dic = dict()
for elem in word:
    word_dic[elem] = 1

if len(word_dic) ==1:# 한글자로만 이루어진 경우
    print(-1)
elif is_palindrome(word, 0, N-1) == True:
    print(len(word) -1)
else:
    print(len(word))
