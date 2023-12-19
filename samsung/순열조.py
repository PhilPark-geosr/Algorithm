import collections
arr = [13, 15, 4, 2]

visited = collections.defaultdict(int)
caselist = []
#순열
def permutation(v, num, p, path):
    if v== p:
        caselist.append(path)
        return
    visited[num] = 1
    for elem in arr:
        if visited[elem] == 0:
            permutation(v+1, elem, p, path+[elem] )
    visited[num] = 0

permutation(0, 0, 3, [])
# print(len(caselist))

# 중복 순열
caselist = []
def product(v, num, p, path):
    if v == p:
        caselist.append(path)
        return
    for elem in arr:
        product(v+1, elem, p, path + [elem])

product(0,0,2, [])
# print(caselist)

caselist = []
def combinations(v, idx, path, p):
    if v==p:
        caselist.append(path)
        return
    for new_idx in range(idx +1, len(arr)):
        combinations(v+1, new_idx, path + [arr[new_idx]], p)
combinations(0, -1, [], 2)
print(caselist)

caselist =[]
def combinations_with_replacement(v, idx, path, p):
    if v == p:
        caselist.append(path)
        return
    for new_idx in range(idx, len(arr)):
        combinations_with_replacement(v+1, new_idx, path + [arr[new_idx]], p)

combinations_with_replacement(0, 0, [], 3)
print(caselist)