import random

class RandomQueue:
    def __init__(self):
        self.items = []
    
    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("Pusta kolejka")

        index = random.randint(0, len(self.items)-1)
        item = self.items[index]

        self.items[index] = self.items[-1]
        self.items.pop()

        return item

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def clear(self):
        self.items = []