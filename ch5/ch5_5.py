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
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return " ".join(result)

    def isEmpty(self):
        return self.head is None
    
    def check(self, data, round = None):
        if round == None:
            if self.isEmpty():
                self.append(data)
            elif data < 0:
                self.append(data)
            else:
                self.add_before(data)
        else:
            if self.isEmpty():
                self.append(data)
            elif data < 0:
                self.append(data)
            else:
                self.add_before_neg(data)

    def add_before_neg(self, data):
        point = Node(data)
        if self.head is None:
            self.head = self.tail = point
            return
        temp = self.head
        while temp and temp.data >= 0:
            temp = temp.next
        if temp is None:
            point.previous = self.tail
            self.tail.next = point
            self.tail = point
        else:
            point.next = temp
            point.previous = temp.previous
            if temp.previous:
                temp.previous.next = point
            else:
                self.head = point
            temp.previous = point

    def append(self, data):
        point = Node(data)
        if self.isEmpty():
            self.head = self.tail = point
        else:
            self.tail.next = point
            point.previous = self.tail
            self.tail = point

    def remove(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.previous:
                    temp.previous.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.previous = temp.previous
                else:
                    self.tail = temp.previous
                return
            temp = temp.next

    def add_before(self, data):
        point = Node(data)
        if self.isEmpty():
            self.head = self.tail = point
        else:
            point.next = self.head
            self.head.previous = point
            self.head = point


def radix_sort(round, big_list):
    divided = 10 ** (round - 1)
    for i in range(10):
        ll = big_list[i]
        temp = ll.head
        while temp:
            t_num = abs(temp.data)
            digit = (t_num // divided) % 10
            nxt = temp.next
            if digit != i:
                ll.remove(temp.data)
                big_list[digit].check(temp.data)
            temp = nxt


def display(round, big_list):
    print(f"Round : {round}")
    for i in range(10):
        print(f"{i} : {big_list[i]}")
    print("------------------------------------------------------------")


big_list = [Linkedlist() for _ in range(10)]
inp = input("Enter Input : ").split()
print("------------------------------------------------------------")

# find_max_digit
max_round = 0
for num in inp:
    t_num = abs(int(num))
    digits = len(str(t_num))
    if digits > max_round:
        max_round = digits

# radix sort process
round = 1
while round <= max_round + 1:
    if round == 1:
        for num in inp:
            num = int(num)
            t_num = abs(num)
            digit = t_num % 10
            big_list[digit].check(num, 1)
    else:
        radix_sort(round, big_list)

    # check if sorting is done early
    if round >= max_round:
        if all(big_list[i].isEmpty() for i in range(1, 10)):
            break

    display(round, big_list)
    round += 1

# result
result = []
for i in range(9, -1, -1):
    temp = big_list[i].head
    while temp:
        result.append(str(temp.data))
        temp = temp.next

print(f"{round - 1} Time(s)")
print(f"Before Radix Sort : {' -> '.join(inp)}")
print(f"After  Radix Sort : {' -> '.join(result)}")
