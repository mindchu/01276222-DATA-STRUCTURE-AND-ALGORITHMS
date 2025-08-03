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
inp = input("input : ").split(",")
count = 0
error_deq = 0
error_inp = 0
for step in inp:
    print(f"Step : {step}")
    if step[0] == "D":
        check = int(step[1])
        i = 0
        while i < check and queue.isEmpty() == False:
            queue.deQueue()
            i += 1
        if check - i != 0:
            error_deq += check - i
        print(f"Dequeue : {queue.items}")
    elif step[0] == "E":
        check = int(step[1:])
        for i in range(check):
            queue.enQueue("*" + str(count))
            count += 1
        print(f"Enqueue : {queue.items}")
    else:
        print(queue.items)
        error_inp += 1
    print(f"Error Dequeue : {error_deq}")
    print(f"Error input : {error_inp}")
    print("--------------------")