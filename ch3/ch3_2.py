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
    
def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
    
def parenMatching(str):
    s = Stack()
    index = 0
    error = 0

    while index < len(str) and error != 1:
        c = str[index]
        if c in '{[(':
            s.push(c)
        if c in '}])':
            if s.size() > 0:
                if not match(s.pop(), c):
                    error = 1
            else:
                error = 2
        index += 1

    if s.size() > 0 and error != 1:
        error = 3
    return error, s

inp = input("Enter expresion : ")
error, s = parenMatching(inp)
if error == 1:
    print(f"{inp} Unmatch open-close")
elif error == 2:
    print(f"{inp} close paren excess")
elif error == 3:
    print(f"{inp} open paren excess   {s.size()} : ",end='')
    for ele in s.items:
        print(ele, sep='', end='')
    print()
else:
    print(f"{inp} MATCH")
