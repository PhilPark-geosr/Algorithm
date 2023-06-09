import sys
sys.stdin = open('input_1343.txt', 'r')

polynomio = input()

def poly_to_list(word):
    s = "" # X 넣을 것들
    t = "" # . 넣을 것들
    result = []
    for elem in word:
        if elem == "X":
            s += elem
            if len(t) !=0: #덜고가야됨
                result.append(t)
                t ="" #t초기화
        else:
            t += elem
            if len(s) !=0: #덜고가야됨
                result.append(s)
                s ="" #t초기화
    if len(s) !=0:
        result.append(s)
    elif len(t) !=0:
        result.append(t)
    else:
        pass
        
    return result

# 변환로직
def change(word):
    result =""
    remain_len_word = len(word)
    while remain_len_word >0:
        if remain_len_word // 4 >= 1: #4로 나눴을때 몫이 1이 넘어가는 경우
            result += "AAAA"*(remain_len_word // 4) # 몫 만큼 추가
            remain_len_word -= 4*(remain_len_word // 4)
        else: # 그 이하로 줄면.. B대입
            result += "BB"*(remain_len_word // 2)
            remain_len_word -= 2*(remain_len_word // 2)
    return result        
polynomio = poly_to_list(polynomio)
# print("polynomio", polynomio)

answer = ""
for elem in polynomio:
    if elem[0] == "X":
        if len(elem)%2 == 1:
            answer = -1
            break
        else:
            answer += change(elem)
            # print(change(elem))
    else:
        answer += elem

print(answer)