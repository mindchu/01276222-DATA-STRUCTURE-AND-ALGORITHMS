class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

def in_to_postfix(str):
    s = Stack()
    index = 0
    result = ''
    operation = {'(':3, '{':3, '[':3, '^':2, '*':1, '/':1, '+':0, '-':0}

    while index < len(str):
        c = str[index]
        if c in '+-*/^({[':
            if s.isEmpty():
                s.push(c)
            while operation[c] <= operation[s.peek()] \
                and s.peek() != '({[':
                result += s.pop()
        else:
            result += c
        


inp = input("Enter Infix : ")
