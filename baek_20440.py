import sys
import collections
sys.stdin = open('input_20440.txt', 'r')
input = sys.stdin.readline
N = int(input())
psum_dic = collections.defaultdict(int)
for _ in range(N):
    S, E = map(int, input().split())
    psum_dic[S] +=1
    psum_dic[E] -=1

# print('psum_dic', psum_dic)

time_list = list(psum_dic.keys())
#시간순 정렬
time_list.sort()


max_cnt = -1
max_s, max_e = -1, -1 #최댓값을 가지는 구간
check = False # 최댓값 가지는 구간 기록 시작했는지 체크하는 변수

cnt = 0 #누적합
for time in time_list:
    # 누적합 업데이트
    cnt += psum_dic[time]
    # 최대구간 갱신
    if cnt > max_cnt:
        max_cnt = cnt
        max_s = time
        check = True
        continue
    if cnt < max_cnt and check ==True: #최대값을 가지다가 딱 떨어지는 그 순간
        max_e = time
        check = False # 최댓값 가지는 구간을 모두 기록했다고 표시
        continue
#결과 출력
print(max_cnt)
print(max_s, max_e)
        
