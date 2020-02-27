import queue
# 이방식은 리스트를 사용하지 않았고, 들어온 순서대로 값을 포인터에 넣는 방식 구현을 하지 못했음.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self,node,data):
        if node == None:
            node = Node(data)

        else:
            if data < node.data:
                node.left = self._insert_value(node.left, data)
                #node.left = data
                #node = Node(data)
                # 아래의 두줄과 위의 한줄의 차이는 ?
                # node.left값에 node값에 객체가 저장될 수있다. 즉 각각의 오른쪽과 왼쪽에 객체들이 들어간 구조가됨
                # node.left의 self._in 이부분이 먼저 시작되어 노드를 만들고 node.left의 값이 정의된다.
                # root에는 전체 오른쪽과 왼쪽으로 나뉜부분이 left,right에 들어가고
                # 그 안의 노드에 서브트리들을 가지고 있는 형태.
                # 최초 data, left right를 가지는 루트노드가 형성되고
                # left안에 서브트리의 루트와 left,rigt를 가지는 노드가 형성되고
                # 다시 이 root.left안의 left와 right에 더 작은 서브트리가 형성되고 각각에 노드형태로 들어간다
                # 즉 처음에는(root) left,right에 가장큰 왼쪽 오른쪽 서브트리가 통으로 들어가고
                # 그 다음에는 다음으로 작은 서브트리가 통으로 들어간다고 이해하면 쉽다.
            else:
                node.right = self._insert_value(node.right, data)
        return node
    # in_order_travalsal방식을 스택으로 구현(dfs방식)
    # def in_odrder_travalsal(self):
    #     node = self.root
    #     stack = [[node,False]] # boolean은 왼쪽방향을 진행했느냐 안했느냐를 표시
    #     self.printall_stack(stack)
    
    # def printall_stack(self, stack):
    #     if len(stack) == 0:
    #         return
    #     node, check = stack.pop(-1)
    #     if check == False:
    #         stack.append([node,True])
    #         if node.left != None:
    #             stack.append([node.left,False])
    #         return self.printall_stack(stack)
    #     else:
    #         print(node.data)
    #         if node.right != None:
    #             stack.append([node.right,False])
    #         return self.printall_stack(stack)
    # # pre_order를 큐를 이용해 구현
    # def pre_order_traversal(self,search_num):
    #     self.search_num = search_num
    #     self.count = 1
    #     self.search_data = 0
    #     node = self.root
    #     que = queue.Queue()
    #     que.put(node)
    #     self.pre_order_search(que)
    #     return self.search_data
        
    
    # def pre_order_search(self,que):
    #     node = que.get()
    #     if self.count == self.search_num:
    #         self.search_data = node.data
    #         return
    #     else:
    #         if node.left != None:
    #             self.count +=1
    #             que.put(node.left)
                
    #         if node.right != None:
    #             self.count += 1
    #             que.put(node.right)
                
    #         self.pre_order_search(que)

    #최초 참조코드
    def pre_order_traversal(self): #self가 있으므로 클래스 객체의 메소드로서 작동하고,
        def _pre_order_traversal(root): #self없이 메소드안에 있으므로 이 메소드 내에서만 동작하는 함수가된다.
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)


tree = tree()
tree.insert(4)
tree.insert(1)
tree.insert(3)
tree.insert(8)
tree.insert(9)
tree.insert(2)
tree.insert(6)
tree.pre_order_traversal()