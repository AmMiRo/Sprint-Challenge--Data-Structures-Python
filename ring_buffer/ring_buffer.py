# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.i_count = 0
#         self.buff = [None]*capacity

#     def append(self, item):
#         self.buff[self.i_count] = item
#         self.i_count += 1
#         if self.i_count == self.capacity:
#             self.i_count = 0

#     def get(self):
#         return [item for item in self.buff if item != None]

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.start = None
        self.head = None
        self.tail = None

    def append(self, item):
        new_node = Node(item)
        if self.count < self.capacity:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
                self.start = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node             
                self.tail.next = self.head
            self.count += 1
        elif self.count == self.capacity:
            if self.tail.next is self.start:
                self.start = new_node
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head.next
            self.head = self.tail.next   

    def get(self):
        data = []
        current = self.start
        while len(data) < self.count:
            data.append(current.value)
            current = current.next
        return data