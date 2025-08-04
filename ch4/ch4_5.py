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

def pt_queue(queue):
    print(f"Queue: {[pos for pos in queue.items]}")

def main():
    width, height, room = input("Enter width, height, and room: ").split()
    try:
        width, height = int(width), int(height)
    except:
        return print("Invalid map input.")
    room = room.split(",")
    if len(room) != height:
        return print("Invalid map input.")
    for r in room:
        if len(r) != width:
            return print("Invalid map input.")
    
    start = None
    for r in range(height):
        for c in range(width):
            if room[r][c] == "F":
                start = (c, r)
                break
        if start:
            break
    if not start:
        return print("Invalid map input.")
    
    search = [[False] * width for _ in range(height)]
    queue = Queue()
    queue.enQueue(start)
    search[start[1]][start[0]] = True
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while not queue.isEmpty():
        pt_queue(queue)
        c, r = queue.deQueue()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                if not search[nr][nc]:
                    cell = room[nr][nc]
                    if cell == '_':
                        search[nr][nc] = True
                        queue.enQueue((nc, nr))
                    elif cell == 'O':
                        return print("Found the exit portal.")
    return print("Cannot reach the exit portal.")

if __name__ == "__main__":
    main()
