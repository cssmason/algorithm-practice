class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = value
        if self.front == - 1:
            self.front = self.rear
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.rear == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.queue) == self.front

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


if __name__ == '__main__':
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1))
    print(myCircularQueue.enQueue(2))
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())
    print(myCircularQueue.isFull())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())
