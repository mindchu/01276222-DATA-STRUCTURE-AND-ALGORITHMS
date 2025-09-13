class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        result = []
        while temp != None:
            result.append(temp.data)
            temp = temp.next
        return "linked list : " + "->".join(result)
    
    def str_reverse(self):
        temp = self.tail
        result = []
        while temp != None:
            result.append(temp.data)
            temp = temp.previous
        return "reverse : " + "->".join(result)
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        point = Node(data)
        if self.isEmpty():
            self.head = point
            self.tail = point
        else:
            point.previous = self.tail
            self.tail.next = point
            self.tail = point

    def insert(self, index, data):
        try:
            index = int(index)
        except:
            return print("Data cannot be added")
        if index < 0:
            return print("Data cannot be added")
        
        point = Node(data)
        if index == 0:
            point.next = self.head
            if self.head != None:
                self.head.previous = point
            else:
                self.tail = point
            self.head = point
            return print(f"index = {index} and data = {data}")
        
        temp = self.head
        for _ in range(index - 1):
            if temp == None:
                return print("Data cannot be added")
            temp = temp.next
        if temp == None:
            return print("Data cannot be added")
        point.next = temp.next
        point.previous = temp
        if temp.next != None:
            temp.next.previous = point
        else:
            self.tail = point
        temp.next = point
        return print(f"index = {index} and data = {data}")
    
    def remove(self, data):
        temp = self.head
        i = 0
        while temp != None:
            if temp.data == data:
                found = i
                if temp.previous != None: 
                    temp.previous.next = temp.next
                else:
                    self.head = temp.next
                if temp.next != None:
                    temp.next.previous = temp.previous
                else:
                    self.tail = temp.previous 
                print(f'removed : {data} from index : {found}')
                return
            temp = temp.next
            i += 1
        print("Not Found!")

    def add_before(self, data):
        point = Node(data)
        if self.isEmpty():
            self.head = point
            self.tail = point
        else:
            point.next = self.head
            self.head.previous = point
            self.head = point

linkedlist = Linkedlist()
inp = input("Enter Input : ").split(",")
for i in inp:
    method, data = i.split()
    if method == "A":
        linkedlist.append(data)
    elif method == "Ab":
        linkedlist.add_before(data)
    elif method == "I":
        index, value = data.split(":")
        linkedlist.insert(index, value)
    elif method == "R":
        linkedlist.remove(data)
    print(linkedlist)
    print(linkedlist.str_reverse())
