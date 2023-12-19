import sys
import collections
sys.stdin = open('input_6443.txt', 'r')
# input = sys.stdin.readline

N = int(input())

def print_anagram(string:list) -> None:
    n = len(string)
    result = []
    visited = collections.defaultdict(int)

    # visited 기록
    for elem in string:
        visited[elem] +=1

    # print(visited)
    def dfs(v, elem, k):
        # print(f"dfs {elem}")
        if v == n-1:
            result.append(elem)
            return
        visited[k] -= 1
        for key in visited:
            if visited[key] > 0:
                dfs(v+1, elem + key, key)
        visited[k] +=1

    for key in visited:
        dfs(0, key, key)

    # print(result)
    for elem in result:
        print(elem)

def string_to_list(string):
    result = []
    for elem in string:
        result.append(elem)
    result.sort()
    return result


for _ in range(N):
    elem = input()
    elem = string_to_list(elem)
    # print(elem)
    print_anagram(elem)