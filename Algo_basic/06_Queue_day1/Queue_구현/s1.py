# Queue 구현

class Queue:
    # Queue 생성자 : 크기가 size인 비어있는 배열을 생성, front와 rear를 -1로 초기화
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.front = -1
        self.rear = -1

    # 큐가 비어있음을 판별하는 인스턴스 메서드
    def is_empty(self):
        return self.front == self.rear

    # 큐가 가득 차있음을 판별하는 인스턴스 메서드
    def is_full(self):
        return self.rear == self.size - 1

    # enQueue 인스턴스 메서드
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
        else:
            self.rear += 1
            self.items[self.rear] = item

    # deQueue 인스턴스 메서드
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            self.front += 1
            return self.items[self.front]


my_queue = Queue(3)

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)     # Queue is full!

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

my_queue.dequeue()     # Queue is empty!
