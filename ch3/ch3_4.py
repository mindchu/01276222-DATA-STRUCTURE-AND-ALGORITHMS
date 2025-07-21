class Calculator:
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
    
    def run(self, instructions):
        if instructions in '+-*/':
            a = self.pop()
            b = self.pop()
            if instructions == '+':
                return self.push(a + b)
            if instructions == '-':
                return self.push(a - b)
            if instructions == '*':
                return self.push(a * b)
            if instructions == '/':
                return self.push(a / b)
        if instructions == 'DUP':
            return self.push(self.peek())
        if instructions == 'POP':
            return self.pop()
        try:
            instructions = int(instructions)
            return self.push(instructions)
        except:
            return False

print("* Stack Calculator *")
inp = input("Enter arguments : ").split()
cal = Calculator()
error = 0
for arg in inp:
    if cal.run(arg) == False:
        print(f"Invalid instruction: {arg}")
        error = 1
        break
if error == 0:
    if cal.isEmpty() == False:
        print(int(cal.peek()))
    else:
        print(0)
