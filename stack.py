class Stack:
    def __init__(self):
        self.storage = []
    def push(self, value):
        self.storage.append(value)
    def pop(self):
        pop_value = self.storage.pop()
        return pop_value
    def print_stack(self):
        print(self.storage)

if __name__ == "__main__":
    stack = Stack()
    data = [1]
    for v in data:
        stack.push(v)
    stack.print_stack()
    stack.push(555)
    stack.print_stack()
    p = stack.pop()
    print(p)
    stack.print_stack()
    p = stack.pop()
    print(p)
    stack.print_stack()
