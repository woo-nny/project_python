# Create the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Create the doubly linked list
class doubly_linked_list:

    def __init__(self):
        self.head = None

# Define the push method to add elements		
    def push(self, NewVal):

        NewNode = Node(NewVal)
        NewNode.next = self.head # 만약 첫번째 값이 들어 온다면, next값은 node
        if self.head is not None: # 2번째 값부터는 head가 바뀌어서 들어오게 된다.
            self.head.prev = NewNode
        self.head = NewNode #여기서 list자체가 가지는 head값을 변경해준다. head가 가장 마지막에 들어온값을 가르킴
    
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
    # Define the append method to add elements at the end
    def append(self, NewVal):

        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
# Define the method to print the linked list 
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

dll = doubly_linked_list()
dll.push(3)
dll.push(8)
dll.push(10)
dll.insert(dll.head.next,4)
dll.listprint(dll.head)