# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left_index = None
#         self.right_index = None

# class Tree:
#     def __init__(self):
#         self.root = []
    
#     def insert_node(self, data):
#         self._insert_node(data,0)

#     def _insert_node(self,data,index):
#         if len(self.root) == index:
#             node = Node(data)
#             self.root.append(node)
#             if index > 0:
#                 if self.root[(index+1)//2-1].left_index == None:
#                     self.root[(index+1)//2-1].left_index = index
#                 else :
#                     self.root[(index+1)//2-1].right_index = index
#         else:
#             if self.root[index].data > data:
#                 a, b = self.root[index].data, data
#                 self.root[index].data = b
#                 self._insert_node(a,index+1)
#             else:
#                 self._insert_node(data,index+1)

#     def print_tree(self):
#         for a in self.root:
#             print(a.data)

# tree = Tree()
# tree.insert_node(2)
# tree.insert_node(5)
# tree.insert_node(3)
# tree.insert_node(1)
# tree.insert_node(8)
# tree.print_tree()


import heapq
T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = list(map(int, input().split()))
    heap = []
    for i in question:
        heapq.heappush(heap, i)
    index = len(heap) - 1
    ans = 0
    while index != 0:
        index = (index+1)//2 -1
        ans += heap[index]
    print("#{} {}".format(t, ans))