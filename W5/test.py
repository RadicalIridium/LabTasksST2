"""
Test file for W5.
Stack code provided by W3Schools: https://www.w3schools.com/python/python_dsa_stacks.asp
"""

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)


# Test the stack implementation
myStack = Stack()

myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)

print("Stack:", myStack.stack)

myStack.pop()
myStack.pop()
myStack.pop()
print("Stack after popping 3 elements:", myStack.stack)