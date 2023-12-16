import sys
from collections import deque
from pprint import pprint
sys.setrecursionlimit(2000000)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = [] # 子ノード
        self.parent = None # 親ノード
        self.subtree_size = 1 # 自分を根とする部分木のサイズ

    def __repr__(self):
        return f"(name: {self.name}, children: {self.children}, parent: {self.parent}, subtree_size: {self.subtree_size}))"

def dfs(tree, root):
    """post ordered DFS"""
    stack = deque()
    stack.append(root)
    tree[root.name].parent = 0
    visited = set()
    while stack:
        node = stack.pop()

        if node in visited:
            # 子ノードをすべて探索した後に実行される
            #print(node) #debug
            # 子ノードのサイズを親ノードに加算する
            if node.parent != 0:
                tree[node.parent].subtree_size += tree[node.name].subtree_size

            continue

        visited.add(node)
        stack.append(node)

        for child in node.children:
            if tree[child].parent is None:
                stack.append(tree[child])
                tree[child].parent = node.name

    return tree


if __name__ == '__main__':
    n = int(input())
    tree = {i:Node(i) for i in range(1, n+1)}
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].children.append(v)
        tree[v].children.append(u)

    # dfsで部分木のサイズを計算
    dfs(tree, tree[1])
    #pprint(tree)

    # node1の部分木のサイズをリストにする
    node1_subtree_size = [tree[i].subtree_size for i in tree[1].children]
    #print(node1_subtree_size)

    # 答えはnode1のすべての部分木のサイズの和から、部分木のサイズの最大値を引いたもの
    ans = sum(node1_subtree_size) - max(node1_subtree_size) + 1 #+1はnode1自身
    print(ans)
