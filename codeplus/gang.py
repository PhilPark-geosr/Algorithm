A = [[1, 3, 5, 7], [3,4,5,6]]

B = [[2, 4, 6, 8], [4,3,2,1]]


def get_merge_array(A,B):
    n = len(A)
    m = len(A[0])
    C = []
    # 시간 복잡도 : O(N^2)
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(A[i][j])
            temp.append(B[i][j])
        C.append(temp)
    return C

print(get_merge_array(A,B))
