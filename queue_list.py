class Queuelist:
    def __init__(self):
        self.storage = []
    def enqueue(self, value):
        self.storage.append(value)
    def dequeue(self):
        if self.storage == []:
            return None
        else:
            dequeue_value = self.storage.pop(0)
            return dequeue_value
    def print_queue(self):
        print(self.storage)

if __name__ == "__main__":
    q = Queuelist()
    data = [1]
    for v in data:
        q.enqueue(v)
    q.print_queue()
    a = q.dequeue()
    print(a)
    q.print_queue()
    q.enqueue(555)
    q.print_queue()
