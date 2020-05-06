class Node:
    def __init__(self,x_location,level,index):
        self.x_location = x_location
        self.left = None
        self.right = None
        self.level = level
        self.index = index
class Tree:
    def __init__(self):
        self.root = None

    def input(self,x_location,level,index):
        self.root = self.input_node(self.root,x_location,level,index)
    
    def input_node(self,node,x_location,level,index):
        if node == None:
            node = Node(x_location,level,index)
        else:
            if x_location < node.x_location:
                node.left = self.input_node(node.left,x_location,level,index)
            else:
                node.right = self.input_node(node.right,x_location,level,index)
        return node

    def preorder(self):
        lis = []
        def preorder(node,lis):
            lis.append(node.index)
            if node.left is not None : preorder(node.left,lis)
            if node.right is not None : preorder(node.right,lis)
        preorder(self.root,lis)
        return lis
    def postorder(self):
        lis = []
        def postorder(node,lis):
            if node.left is not None : postorder(node.left,lis)
            if node.right is not None : postorder(node.right,lis)
            lis.append(node.index)
        postorder(self.root,lis)
        return lis



def solution(nodeinfo):
    # import sys    재귀제한을 임으로 풀어줌
    # sys.setrecursionlimit(10**6)
    level_dic = {}
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x:(-x[1],x[0]))
    tree = Tree()
    for node in nodeinfo:
        x,y,z = node
        tree.input(x,y,z)
    return [tree.preorder(),tree.postorder()]


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfo)