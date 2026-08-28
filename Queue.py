class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, ticket):
        if self.rear == self.size - 1:
            print("Queue is Full")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue[self.rear] = ticket
            print("Ticket", ticket, "added to queue")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is Empty")
        else:
            print("Ticket", self.queue[self.front], "served")
            self.front += 1

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is Empty")
        else:
            print("Tickets in queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Main program
q = Queue(5)

q.enqueue(101)
q.enqueue(102)
q.enqueue(103)

q.display()

q.dequeue()
q.dequeue()

q.display()

q.enqueue(104)
q.enqueue(105)

q.display()
