class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    def append(self, value):
        cursor = self
        while cursor.next != None:
            cursor = cursor.next
        cursor.next = LinkedList(value)
    def pop(self):
        cursor = self
        if cursor.next == None:
            pop_value = cursor.value
            return "Front " + str(pop_value)
        else:
            while cursor.next.next != None:
                cursor = cursor.next
            pop_value = cursor.next.value
            cursor.next = None
        return pop_value
    def pop_i(self, i):
        cursor = self
        if i == 0:
            return "Front"
        else:
            cont = 0
            while cursor.next.next != None:
                if cont + 1 == i:
                    pop_value = cursor.next.value
                    cursor.next = cursor.next.next
                    return pop_value
                else:
                    cursor = cursor.next
                    cont += 1
            if cont + 1 == i:
                pop_value = self.pop()
                return pop_value
            elif cont + 1 < i:
                pop_value = None
        return pop_value
    def __repr__(self):
        s = '['
        cursor = self
        while cursor != None:
            s += str(cursor.value)
            s += ','
            cursor = cursor.next
        s += ']'
        return s

if __name__ == "__main__":
    data = [1,2]
    ll = LinkedList(data.pop(0))
    for v in data:
        ll.append(v)
    print(ll)
    a = ll.pop_i(1)
    print(a)
    print(ll)
