import sys
import collections

sys.stdin = open('input_4256.txt','r')
input = sys.stdin.readline

# functionality

class TreeNode():
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def make_tree(inorder):

    if len(inorder) ==0:
        return None
    
    val = postorder.popleft() #루트노드 추출
    
    # 노드 생성
    root = TreeNode(val)
    # inorder에서 좌우 찾기
    idx = inorder.index(val)

    left_list = inorder[:idx]
    right_list = inorder[idx+1:]

    root.left = make_tree(left_list)
    root.right = make_tree(right_list)

    return root

def dfs(node):
    if node == None:
        return 
    
    dfs(node.left)
    dfs(node.right)
    result.append(node.val)



T = int(input())
for _ in range(T):
    N = int(input())
    postorder = collections.deque(map(int, input().split()))
    inorder = list(map(int, input().split()))

    tree = make_tree(inorder)

    result = []
    dfs(tree)
    for elem in result:
        print(elem, end = " ")
    print()
   
