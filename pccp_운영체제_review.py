def solution(program):
    # 프로그램 딜레이 시간 리스트
    n = len(program)
    delay_list = [0]*(n+1)
    # 호출시간, 점수 순으로 정렬
    program.sort(key =lambda x: x[1])

    # 끝나는 시간 구하기


