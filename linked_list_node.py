class Linkedlist:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
        else:
            cursor = self.head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = new_node
    def append_node(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            cursor = self.head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = new_node
            new_node.next = None
    def pop(self, i):
        cursor = self.head
        if self.head == None:
            return None
        else:
            if i == -1:
                if cursor.next == None:
                    pop_value = cursor.value
                    self.head = None
                    return pop_value
                while cursor.next.next != None:
                    cursor = cursor.next
                pop_value = cursor.next.value
                cursor.next = None
                return pop_value
            elif i == 0:
                pop_value = cursor.value
                self.head = cursor.next
                return pop_value
            else:
                cont = 0
                if cursor.next == None:
                    if i != 0 or -1:
                        return None
                while cursor.next.next != None:
                    if cont + 1 == i:
                        pop_value = cursor.next.value
                        cursor.next = cursor.next.next
                        return pop_value
                    else:
                        cont += 1
                        cursor = cursor.next
                if cont + 1 == i:
                    pop_value = self.pop(-1)
                    return pop_value
                elif cont + 1 < i:
                    return None
    def pop_front_node(self):
        pop_node = self.head
        self.head = self.head.next
        pop_node.next = None
        return pop_node

            

    def __repr__(self):
        s = "["
        cursor = self.head
        while cursor != None:
            s += str(cursor.value)
            s += ","
            cursor = cursor.next
        s += "]"
        return s

if __name__ == "__main__":
    ll = Linkedlist()
    data = [1,2,3,4,5]
    for v in data:
        ll.append(v)
    print(ll)
    a = ll.pop(0)
    print(a)
    print(ll)
    b = ll.pop_front_node()
    print(b)
    print(ll)