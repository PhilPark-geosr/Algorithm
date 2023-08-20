import sys
sys.stdin = open('input_1062.txt', 'r')


N, K = map(int, input().split())
word_list = []
for _ in range(N):
    s = input()
    word_list.append(s)

# 비트마스크로 변환하기
word_mask = []
for word in word_list:
    mask = 0
    for s in word:
        bit = (1<<(ord(s) - ord('a')))
        # print('bit', s, ord(s) - ord('a'), bit)
        mask |= bit
    word_mask.append(mask)

# print('work_mask',word_mask)

def check(target_bit, base_bit):
    # base_bit가 target_bit 포함하고 있는지 검사
    if target_bit&base_bit == target_bit:
        return True
    return False
        
if K < 5:
    print(0)
else:
    # caselist만들기
    import itertools
    candidiate = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    caselist = list(map(list, itertools.combinations(candidiate, K-5)))
    pre_exist = ['a','c','t','i','n']
    # print(caselist)
    case_bit_list = []
    for case in caselist:
        case = case + pre_exist
        # print(case)
        mask = 0
        # 비트 마스크 기록
        for elem in case:
            mask |= (1<<(ord(elem)-ord("a")))
        case_bit_list.append(mask)
    # print(case_bit_list)

    '''
    antarctica
    antahellotica
    antacartica
    '''


    # 검사
    answer = 0
    for case_bit in case_bit_list:

        cnt = 0
        for word_bit in word_mask:
            if check(word_bit, case_bit) == True: #배울수 있는 단어인지 체크
                cnt +=1

        if cnt > answer:
            answer = cnt


    print(answer)