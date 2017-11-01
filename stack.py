class Node:

	next = None;

	def __init__(self, item):
		self.value = item


class Stack:

	top = None;

	def push(self, item):
		node = Node(item)
		node.next = self.top
		self.top = node

	def pop(self):
		self.top = self.top.next

	def peek(self):
		return self.top.value

