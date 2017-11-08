class Node:
    def __init__(self, item):
        self.value = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.first = None

    def AddLast(self, _item):
        item = Node(_item)
        if self.first == None:
            self.first = item
        else:
            node = self.first

            while(node.next != None):
                node = node.next
            node.next = item
    
    def AddFirst(self, _item):
        item = Node(_item)
        tmp = self.first
        self.first = item
        item.next = tmp

    def RemoveFirst(self):
        Remove(self.first)

    def Remove(self, node):
        tmp = node.next
        prev = self.first
        if self.first == node:
            self.first = tmp
        else:
            while(prev.next != node):
                    prev = prev.next
            prev.next = tmp
        

    

        
        
