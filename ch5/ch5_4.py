class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

class Vim:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None

    def insert(self, data):
        point = Node(data)
        if self.head == None:
            self.head = point
            self.tail = point
            self.cursor = point
        else:
            if self.cursor == None:
                point.next = self.head
                self.head.previous = point
                self.head = point
                self.cursor = point
            else:
                point.next = self.cursor.next
                point.previous = self.cursor
                if self.cursor.next != None:
                    self.cursor.next.previous = point
                else:
                    self.tail = point
                self.cursor.next = point
                self.cursor = point

    def move_left(self):
        if self.cursor != None:
            self.cursor = self.cursor.previous

    def move_right(self):
        if self.cursor == None:
            if self.head != None:
                self.cursor = self.head
        elif self.cursor.next != None:
            self.cursor = self.cursor.next

    def backspace(self):
        if self.cursor == None:
            return
        point = self.cursor
        if point.previous != None:
            point.previous.next = point.next
        else:
            self.head = point.next
        if point.next != None:
            point.next.previous = point.previous
        else:
            self.tail = point.previous
        self.cursor = point.previous

    def delete(self):
        if self.cursor == None:
            point = self.head
        else:
            point = self.cursor.next
        if point == None:
            return
        if point.previous != None:
            point.previous.next = point.next
        else:
            self.head = point.next
        if point.next != None:
            point.next.previous = point.previous
        else:
            self.tail = point.previous

    def result(self):
        text = []
        temp = self.head
        while temp != None:
            text.append(temp.data)
            if temp == self.cursor:
                text.append("|")
            temp = temp.next
        if self.cursor == None:
            text.insert(0, "|")
        return " ".join(text)

vim = Vim()
inp = input("Enter Input : ").split(",")
for i in inp:
    if i in ["L", "R", "B", "D"]:
        if i == "L":
            vim.move_left()
        elif i == "R":
            vim.move_right()
        elif i == "B":
            vim.backspace()
        elif i == "D":
            vim.delete()
    elif i.startswith("I"):
        method, data = i.split()
        vim.insert(data)
print(vim.result())