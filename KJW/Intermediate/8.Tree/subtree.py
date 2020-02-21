class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self,cnt):
        self.node_list=[None]
        for i in range(E+1):
            self.node_list.append(Node(i))
    
    def put(self,parent,child):
        if self.node_list[parent].left == None: # 왼쪽에 노드가 없다면
            self.node_list[parent].left = self.node_list[child] # 왼쪽에 자식 노드 추가
        else:
            self.node_list[parent].right = self.node_list[child] # 오른쪽에 노드가 없다면 오른쪽 자식 노드 추가
    def count(self,node):
        self.cnt += 1
        if node.left != None: # 노드 왼쪽 확인
            self.count(node.left)
        if node.right != None: # 노드 오른쪽 확인
            self.count(node.right)
    def result(self,num):
        self.cnt = 0
        self.count(self.node_list[num])
        return self.cnt

T =int(input())

for T in range(T):
    E, N = map(int, input().split())
    data = list(map(int,input().split()))
    tree = Tree(E)
    for i in range(E):
         tree.put(data[2*i],data[2*i+1]) # 자식 노드 오른쪽 왼쪽
    print("#{} {}".format(T+1,tree.result(N)))