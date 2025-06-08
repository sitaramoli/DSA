class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "List is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "List is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return f"{self.queue}"


myQueue = Queue()
myQueue.dequeue()
myQueue.enqueue(3)
myQueue.enqueue(2)
myQueue.enqueue(1)
print("Peek: ",myQueue.peek())
myQueue.dequeue()
print("Queue: ", myQueue)
