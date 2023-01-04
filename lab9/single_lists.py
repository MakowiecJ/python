class SingleList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
# ... inne metody ...

    def remove_tail(self):    # klasy O(n)
        if self.is_empty(): 
            raise ValueError('Lista jest pusta')

        node = self.head
        while node.next != self.tail:
            node = node.next

        deletedNode = node.next
        node.next = None
        self.length -= 1
        return deletedNode
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.

    def join(self, other):   # klasy O(1)
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        other.clear()
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):   # czyszczenie listy
        self.head = None
        self.tail = None
        self.lenght = 0