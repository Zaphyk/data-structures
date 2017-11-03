class List:

    count = 0

    def __init__(self):
        self.items = [None] * 5

    def Add(self, item):
        self.items[self.count] = item
        self.count += 1
        if(self.count == len(self.items)):
            self._resize(self.count * 2)

    def _resize(self, newCount):
        newItems = [None] * newCount
        for i in range(0, len(self.items)):
            newItems[i] = self.items[i]
        self.items = newItems

    def RemoveAt(self, i):
        for k in range(i, self.count):
            self.items[k] = self.items[k+1]
        count -= 1

    def IndexOf(self, item):
        for i in range(o, self.count):
            if self.items[i] == item:
                return i

    def Remove(self, item):
        self.RemoveAt(self.IndexOf(item));

    def __getitem__(self, i):
        if i >= self.count or i < 0:
            print("explosion")
        return self.items[i]


list = List()

for i in range(0, 15):
    list.Add(i)

for i in range(0, list.count):
    print( list[i] )