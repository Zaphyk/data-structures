class Queue:

    def __init__(self):
        self.count = 0

    def Queue(self, item):
        node = Node(item)
        if self.count == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.count += 1

    def Dequeue(self):
        node = self.first
        self.first = self.first.next
        self.count -= 1
        return node.item

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None

queue = Queue()
queue.Queue( "random string" )
queue.Queue( [0,1,3,2,4] )
queue.Queue( 9.324 )

for i in range(0, 3):
	print(queue.Dequeue())