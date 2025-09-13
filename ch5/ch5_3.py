class node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = None
    tail = None
    for data in l:
        point = node(int(data))
        if head == None:
            head = point
            tail = point
        else:
            tail.next = point
            tail = point
    return head

def printList(H):
    temp = H
    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def mergeOrderesList(p,q):
    if p == None:
        return q
    if q == None:
        return p
    if p.data < q.data:
        p.next = mergeOrderesList(p.next, q)
        return p
    else:
        q.next = mergeOrderesList(p, q.next)
        return q

#################### FIX comand ####################   
# input only a number save in L1,L2
L1, L2 = input("Enter 2 Lists : ").split()
L1 = L1.split(",")
L2 = L2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)