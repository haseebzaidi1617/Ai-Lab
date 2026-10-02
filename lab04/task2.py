#queue implementatin 
class Queue:

    def __init__(self):
        self.queue = []   # create queue

    # add element to queue
    def enqueue(self, value):
        self.queue.append(value)
        print(value, "added into queue")

    # remove element from queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            value = self.queue.pop(0)
            print(value, "removed from queue")

    # display front element
    def Front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # display all elements
    def display(self):
        print("Queue:", self.queue)


# create queue object
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()
q.Front()

q.dequeue()
q.display()
q.Front()