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
        if c in '({[':
            s.push(c)
        elif c in ')}]':
            if c == ')':
                while s.peek() != '(':
                    result += s.pop()
            if c == '}':
                while s.peek() != '{':
                    result += s.pop()
            if c == ']':
                while s.peek() != '[':
                    result += s.pop()
            s.pop()
        elif c in '+-*/^':
            while s.isEmpty() == False \
                and s.peek() not in '({[' \
                and operation[c] <= operation[s.peek()]:
                result += s.pop()
            s.push(c)
        else:
            result += c
        index += 1
    while s.isEmpty() == False:
        result += s.pop()
    return result

inp = input("Enter Infix : ")
print(f"Postfix : {in_to_postfix(inp)}")
