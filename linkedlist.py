class Node:
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.data}: {self.next_node}"

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def append_node(self, node: Node):
        """ adds the given node to the end of the linked list """
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next_node:
                curr = curr.next_node
            curr.next_node = node
        return self.head

    def add(self, data):
        """ creates and adds a new node at the head of the linked list """
        node = Node(data)
        node.next_node = self.head
        self.head = node

    def find(self, data):
        current = self.head
        idx = 0
        while current:
            if current.data == data:
                return current
            current = current.next_node
            idx += 1
    
    def remove(self, data):
        """
            finds and deletes the node containing the given data
            1: 2: 25: 26: 3: 4: None
        """
        if self.head.data == data:
            self.head = self.head.next_node
        else:
            prev_node = None
            current_node = self.head
            while current_node.data != data:
                prev_node = current_node
                current_node = current_node.next_node
            prev_node.next_node = current_node.next_node
        return self.head

    def insert_at(self, data, index):
        """
            creates a new node and inserts it at the given index
        """
        if index == 0:
            self.add(data)
            return self.head
        new_node = Node(data)
        prev_node = None
        pos = 0
        current = self.head 
        while pos < index:
            prev_node = current
            current = current.next_node
            pos += 1
        prev_node.next_node = new_node
        new_node.next_node = current
    
    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count


"""
n1 = Node(10)
# n2 = Node(20)
n1.next_node = n2

ll = LinkedList()
# ll.size()
ll.append_node(n1)
ll.size()

"""