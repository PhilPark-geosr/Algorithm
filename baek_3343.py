import sys
sys.stdin = open('input_3343.txt', 'r')

N, A, B, C, D = map(int, input().split())


# 우선순위 결정
priority = None
secondary = None
if B/A < D/C:
    priority = (A, B)
    secondary = (C, D)
elif B/A == D/C:
    if A <= C:
        priority = (A, B)
        secondary = (C, D)
    else:
        priority = (C, D)
        secondary = (A, B)
else: # B/A > D/C:
    priority = (C, D)
    secondary = (A, B)

# 가성비로 다 때려박은것부터 확인
def extract_max(target, case):
    result = target - (target // case[0]) * case[0]
    cost = (target // case[0]) * case[1]
    cnt = (target // case[0])
    if result >0:
        cnt += 1
        cost += case[1]
    return cnt, cost

max_cnt, max_cost = extract_max(N, priority)
# print(max_cnt, max_cost)

#줄여가면서 확인
answer = max_cost
n= max_cnt


def cal_cost(N, n):
    #n개 가성비 코스로 비용 개산하기
    cost = priority[1]*n
    # 이제 몇개 남았는지 확인
    res = N - n*priority[0]

    return res, cost


while n>0:
    # print(answer)
    # 가성비 갯수 하나 줄이기
    n -=1
    res, efficient_cost = cal_cost(N, n)

    # 남은 res계산
    cnt, cost = extract_max(res, secondary)
    # print(f"efficient_cost, cost", efficient_cost, cost)
    # if efficient_cost + cost >=answer:
    #     break
    answer = min(answer, efficient_cost + cost)

print(answer)