MAX_SIZE = 101
a = [0] * MAX_SIZE
front = 0
rear = -1
current_size = 0

def isEmpty():
    return current_size == 0

def isFull():
    return current_size == MAX_SIZE

def size():
    return current_size

def enqueue(item):
    global rear, current_size
    if isFull():
        print("Queue is full. Cannot enqueue.")
        return
    rear = (rear + 1) % MAX_SIZE
    a[rear] = item
    current_size += 1

def dequeue():
    global front, current_size
    if isEmpty():
        print("Queue is empty. Cannot dequeue.")
        return -1
    removed_item = a[front]
    front = (front + 1) % MAX_SIZE
    current_size -= 1
    return removed_item
