
__import__("stack")

stack = Stack()
stack.push( "random string" )
stack.push( [0,1,3,2,4] )
stack.push( 9.324 )

for i in range(0, 3):
	print(stack.peek())
	stack.pop()

#	RESULT
#	
#	9.324
#	[0, 1, 3, 2, 4]
#	random string