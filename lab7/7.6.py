import random

class It1:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a = (x + 1) % 2
        return x

class It2:
    def __iter__(self):
        self.l = ['N', 'E', 'S', 'W']
        return self

    def __next__(self):
        x = random.choice(self.l)
        return x

class It3:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a = (x + 1) % 7
        return x


it1 = It1()
iter1 = iter(it1)

it2 = It2()
iter2 = iter(it2)

it3 = It3()
iter3 = iter(it3)

l = []
for i in range(10):
    l.append(next(iter1))
print(l)


l = []
for i in range(10):
    l.append(next(iter2))
print(l)


l = []
for i in range(10):
    l.append(next(iter3))
print(l)