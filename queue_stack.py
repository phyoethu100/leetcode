# Queues Question #12 - Queue with Stacks

class QueueStacks:

    def __init__(self):
        self.inside = []
        self.outside = []
    
    def enqueue(self, value): # O(1)
        self.inside.append(value)

    def dequeue(self): # O(n)
        if (len(self.outside) == 0):
            while (len(self.inside)):
                self.outside.append(self.inside.pop())
        
        return self.outside.pop()
    
    def peek(self): # O(n)
        if (len(self.outside) == 0):
            while (len(self.inside)):
                self.outside.append(self.inside.pop)
        
        return self.outside[len(self.outside) - 1]
    
    def empty(self): # O(1)
        return len(self.inside) == 0 and len(self.outside) == 0


queue = QueueStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("After enqueue...")
print(queue.inside)
print(queue.outside)

queue.dequeue()
print("After dequeue...")
print(queue.inside)
print(queue.outside)

print("After peek...")
print(queue.peek())

print("After empty...")
print(queue.empty())