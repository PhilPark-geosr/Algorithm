import sys
sys.stdin = open('input_12970.txt', 'r')
N, K = map(int, input().split())

def solution(N, K):
    answer = -1
    if K > (N//2)*(N-N//2):
        return answer
    
    # a+b <= N, a*b = K인거 찾기
    a = 0
    b = 0
    while a<=b:
        if a*b ==K  and a + b <=N:
            break
        a+=1
        b = int(K/a)
    # 기준 다 통과하면
    if a + b <=N and a*b == K:
        
        answer = "A"*a + "B"*b + "A"*(N-(a+b))
        return answer

    else:
        return answer
    # 이제 다 통과됐으니..
    # a, b나왔을것

print(solution(N, K))