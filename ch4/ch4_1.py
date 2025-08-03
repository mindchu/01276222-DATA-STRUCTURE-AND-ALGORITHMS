class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

queue = Queue() 
inp = input("Enter Input : ").split(",")
for item in inp:
    value = item.split()
    if len(value) > 1:
        queue.enQueue(value[1])
        print(f"Add {value[1]} index is {queue.size() - 1}")
    else:
        if queue.isEmpty():
            print("-1")
        else:
            print(f"Pop {queue.deQueue()} size in queue is {queue.size()}")
if queue.isEmpty():
    print("Empty")
else:
    print(f"Number in Queue is :  {queue.items}")