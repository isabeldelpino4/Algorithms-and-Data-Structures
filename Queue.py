class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        """Insert item at the back of the queue (enqueue)."""
        self.items.append(item)

    def delete(self):
        """Remove and return the front item (dequeue)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def pop(self):
        """Top item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def __str__(self):
        return "Queue: " + str(self.items)


# DEMO 
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q)             # Queue: [10, 20, 30]
print(q.pop())       # 10 (front element)
print(q.delete())    # 10 (removed from front)
print(q)             # Queue: [20, 30]
