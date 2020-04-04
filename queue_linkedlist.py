from linked_list_node import Linkedlist
class Queuelinkedlist:
    def __init__(self):
        self.storage = Linkedlist()
    def enqueue(self, value):
        self.storage.append(value)
    def enqueue_node(self, new_node):
        self.storage.append_node(new_node)
    def dequeue(self):
        dequeue_value = self.storage.pop(0)
        return dequeue_value
    def dequeue_cat(self, value):
        compare = self.storage.pop_front_node()
        if compare.value == value:
            return value
        else:
            divide = Linkedlist.Node(0)
            self.enqueue_node(divide)
            self.enqueue_node(compare)
            compare = self.storage.pop_front_node()
            while compare != divide:
                if compare.value != value:
                    self.enqueue_node(compare)
                    compare = self.storage.pop_front_node()
                else:
                    compare = self.storage.pop_front_node()
                    while compare != divide:
                        self.enqueue_node(compare)
                        compare = self.storage.pop_front_node()
                    return value
            return None
                

                

    def print_queue(self):
        print(self.storage.__repr__())

q = Queuelinkedlist()
data = [2,3,4,5,1]
for v in data:
    q.enqueue(v)
q.print_queue()
# q.enqueue(555)
# q.print_queue()
# a = q.dequeue()
# print(a)
# q.print_queue()
# a = q.dequeue()
# print(a)
# q.print_queue()
leave = q.dequeue_cat(1)
print(leave)
q.print_queue()

