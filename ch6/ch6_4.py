def display(maxn, source=None, destination=None):
    global A, B, C
    if source and destination:
        if source == 'A':
            if destination == 'B':
                B.append(A.pop())
            else:
                C.append(A.pop())
        elif source == 'B':
            if destination == 'A':
                A.append(B.pop())
            else:
                C.append(B.pop())
        else:
            if destination == 'A':
                A.append(C.pop())
            else:
                B.append(C.pop())
    rods = [A, B, C]
    result = []
    for rod in rods:
        temp = ['|'] * (maxn - len(rod)) + list(reversed(rod))
        result.append(temp)
    for i in range(maxn):
        print(f"{result[0][i]}  {result[1][i]}  {result[2][i]}")

def move(n,A,B,C,maxn):
    if n == 1:
        print(f"move {n} from  {A} to {C}")
        display(maxn, A, C)
    else:
        move(n - 1, A, C, B, maxn)
        print(f"move {n} from  {A} to {C}")
        display(maxn, A, C)
        move(n - 1, B, A, C, maxn)

n = int(input("Enter Input : "))
A = list(range(n, 0, -1))
B = []
C = []
display(n + 1)
move(n, 'A', 'B', 'C', n + 1)