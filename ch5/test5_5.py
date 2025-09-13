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
    
    def check(self, data):
        """Insert with rule: positives before negatives."""
        if self.isEmpty():
            self.append(data)
        elif data >= 0:
            self.add_before_neg(data)
        else:
            self.append(data)

    def add_before_neg(self, data):
        """Insert data before first negative; if no negatives, append."""
        point = Node(data)
        if self.head is None:
            self.head = self.tail = point
            return

        temp = self.head
        while temp and temp.data >= 0:
            temp = temp.next

        if temp is None:  # no negatives found → append
            point.previous = self.tail
            self.tail.next = point
            self.tail = point
        else:  # insert before first negative
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

    def remove_node(self, node):
        """Remove by node reference (faster than searching)."""
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous


def radix_sort(round, big_list):
    divided = 10 ** (round - 1)
    for i in range(10):
        ll = big_list[i]
        temp = ll.head
        while temp:
            nxt = temp.next
            digit = abs(temp.data) // divided % 10
            if digit != i:
                ll.remove_node(temp)
                big_list[digit].check(temp.data)
            temp = nxt


def display(round, big_list):
    print(f"Round : {round}")
    for i in range(10):
        print(f"{i} : {big_list[i]}")
    print("------------------------------------------------------------")


# main
big_list = [Linkedlist() for _ in range(10)]
inp = input("Enter Input : ").split()
print("------------------------------------------------------------")

# find max digit length
max_round = max(len(str(abs(int(num)))) for num in inp)

# radix sort process
round = 1
while round <= max_round + 1:
    if round == 1:
        for num in inp:
            num = int(num)
            digit = abs(num) % 10
            big_list[digit].check(num)
    else:
        radix_sort(round, big_list)

    # check if sorting is done early
    if round >= max_round and all(big_list[i].isEmpty() for i in range(1, 10)):
        break

    display(round, big_list)
    round += 1

# collect result
result = []
for i in range(9, -1, -1):
    temp = big_list[i].head
    while temp:
        result.append(str(temp.data))
        temp = temp.next

print(f"{round - 1} Time(s)")
print(f"Before Radix Sort : {' -> '.join(inp)}")
print(f"After  Radix Sort : {' -> '.join(result)}")
