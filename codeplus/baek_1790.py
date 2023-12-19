import sys
sys.stdin =open('input_1790.txt','r')
N, K =map(int, input().split())

def get_len(num):
    n = len(str(num)) # 몇자리 수인지 구한다
    cnt = 0
    for i in range(n-1):
        cnt += 9*(10**i)*(i+1)
    cnt += (num- 10**(n-1)+1)*n
    return cnt

# test
# print(get_len(12))

#
def binary_search():
    l = 1
    r = N
    answer =-1
    answer_len = -1
    while l<=r:
        mid = (l+r)//2
        length = get_len(mid) #1 ~ mid로 만든 수의 길이
        if length < K:
            l = mid +1
        elif length == K:
            answer = mid
            answer_len = length
            break
        else:
            answer = mid
            answer_len = length
            r =mid -1
    return answer_len, answer
answer_len, answer = binary_search()
if answer ==-1:
    print(answer)
else:
    answer = str(answer)
    # print(answer)
    idx = answer_len - K
    n = len(answer)
    answer = int(answer[n-1-idx])
    print(answer)