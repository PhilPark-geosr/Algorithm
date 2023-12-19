def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]  # 목표값

    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])

    # dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    dp = [[-1] * (150 + 1) for _ in range(150 + 1)]

    # alp = min(alp, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    # cop = min(cop, max_cop_req)
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    # dp[alp][cop] = 0  # dp[i][j]의 의미 : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간
    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[i][j] = 0

    def dfs(i, j):

        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = float('inf')
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if i - alp_rwd >= alp_req and j - cop_rwd >= cop_req:
                dp[i][j] = min(dp[i][j], dfs(i - alp_rwd, j - cop_rwd) + cost)

        return dp[i][j]

    answer = float('inf')
    for i in range(max_alp_req, 151):
        for j in range(max_cop_req, 151):
            answer = min(answer, dfs(i, j))
    # answer = dfs(max_alp_req, max_cop_req)
    return answer