class Queue:
    def __init__(self, list=None):
        self.items = list if list else []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Customer:
    def __init__(self, customer_no, arrive, make_time):
        self.customer_no = customer_no
        self.arrive = arrive
        self.make_time = make_time
        self.finish = None

    def find_wait_time(self):
        return (self.finish - self.arrive) - self.make_time

def process_baristas(baristas, time, queue, finish):
    finished_customers = []

    for barista in baristas:
        if len(barista) > 0 and barista[0].finish == time:
            finished_customers.append(barista.pop(0))
    finished_customers.sort(key=lambda c: c.customer_no)

    for c in finished_customers:
        finish.enQueue(c)

    for barista in baristas:
        if len(barista) == 0 and not queue.isEmpty():
            customer = queue.deQueue()
            customer.finish = time + customer.make_time
            barista.append(customer)

    return finished_customers

print(" ***Cafe***")
inp = input("Log : ").split("/")
log = []
customer_no = 1
for i in inp:
    arrive, make_time = [int(item) for item in i.split(",")]
    log.append(Customer(customer_no, arrive, make_time))
    customer_no += 1

queue = Queue()
finish = Queue()
barista1 = []
barista2 = []
baristas = [barista1, barista2]

time = 0
while finish.size() != len(inp):
    while len(log) > 0 and log[0].arrive == time:
        queue.enQueue(log.pop(0))
    process_baristas(baristas, time, queue, finish)
    time += 1

longest = None
while not finish.isEmpty():
    c = finish.deQueue()
    print(f"Time {c.finish} customer {c.customer_no} get coffee")
    if longest == None:
        longest = c
    elif c.find_wait_time() >= longest.find_wait_time():
        longest = c

if longest.find_wait_time() == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {longest.customer_no}")
    print(f"The customer waited for {longest.find_wait_time()} minutes")
