from linked_list import Linkedlist

class Queue:
    def __init__(self):
        self.storage = Linkedlist()
    def push(self, value):
        self.storage.append(value)
    def push_node(self, node):
        self.storage.append_node(node)
    def popany(self):
        leave = self.storage.head
        self.storage.head = self.storage.head.next
        return leave.value
    def pop1(self):
        if self.storage.head == None:
            return None
        else:
            cursor = self.storage.head
            first = self.storage.head
            if first.value == 1:
                leave = first
                self.storage.head = self.storage.head.next
            else:
                self.storage.head = first.next
                self.push_node(first)
                cursor = self.storage.head
                while cursor.value != 1 and cursor != first:
                    self.storage.head = cursor.next
                    self.push_node(cursor)
                    cursor = self.storage.head
                if cursor == first:
                    return None
                elif cursor.value == 1:
                    leave = cursor
                    cursor = cursor.next
                    while cursor != first:
                        self.storage.head = cursor.next
                        self.push_node(cursor)
                        cursor = self.storage.head
                return leave.value
    def __repr__(self):
        return self.storage.__repr__()
    
        
data = [1,2,3,1,4,5]
q = Queue()
l = Linkedlist()
for v in data:
    l.append(v)
print(l)
for v in data:
    q.push(v)
print(q)
q.push(3)
print(q)
print(q.popany())
print(q)
print(q.pop1())
print(q)
print(q.pop1())
print(q)
