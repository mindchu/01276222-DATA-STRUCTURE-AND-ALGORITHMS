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

main = Queue()
cash1 = Queue()
cash2 = Queue()
inp = input("Enter people : ")
for people in inp:
    main.enQueue(people)
count = 1
time_cash1 = 0
time_cash2 = 0
while main.isEmpty() == False:
    if cash1.isEmpty() == False:
        time_cash1 += 1
        if time_cash1 == 3:
            cash1.deQueue()
            time_cash1 = 0
    if cash2.isEmpty() == False:
        time_cash2 += 1
        if time_cash2 == 2:
            cash2.deQueue()
            time_cash2 = 0
    if cash1.size() < 5:
        cash1.enQueue(main.deQueue())
    elif cash2.size() < 5:
        cash2.enQueue(main.deQueue())
    print(f"{count} {main.items} {cash1.items} {cash2.items}")
    count += 1
