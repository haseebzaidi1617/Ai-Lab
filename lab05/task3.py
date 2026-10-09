# Task 3: Priority Queue Implementation

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, data, priority):
        # List (data, priority) append data
        self.queue.append((data, priority))

    def pop(self):
        if self.is_empty():
            print("Queue empty !")
            return None

        # Minimum priority number element find(Highest Priority)
        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[min_index][1]:
                min_index = i

        # Element return after pop
        item = self.queue.pop(min_index)
        return item[0], item[1]

    def is_empty(self):
        return len(self.queue) == 0


# --- Execution ---
pq = PriorityQueue()

pq.push("A", 3)
pq.push("B", 1)
pq.push("C", 2)

while not pq.is_empty():
    data, priority = pq.pop()
    print(f"Data: {data}, Priority: {priority}")