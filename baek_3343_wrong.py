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

# 일단 우선순위로 최대한 뺼수 있는데 까지 뺀다
def extract_max(N, priority):

    result = N - (N//priority[0])*priority[0]
    cost = (N//priority[0])*priority[1]
    return result, cost

total_cost = 0
res, cost = extract_max(N, priority)
total_cost += cost
#print(total_cost, res)

# 나머지를 어떤걸로 할지 테스트
def cal_money(res, case, compare):

    cost = 0
    while res>0:
        res -= case[0]
        cost += case[1]
        if cost >= compare:
            return compare #그냥 원래꺼 쓰자

    return cost



money1 = priority[1]
money2 = cal_money(res, secondary, money1)

#print(money1, money2)

answer = total_cost + money2
print(answer)