"""

Implement a stack (push, pop, peek).


STEPS


1 - class Stack: - Defines a new class called Stack
2 - def __init__(self): - Constructor method that runs when a new Stack
    object is created

3 - self.items = [] - Creates an empty list to store stack elements.
    self refers to the current object instance.
4 - def push(self, item): - Method to add items to the stack

5 - self.items.append(item) - Adds the item to the end of the list
    (top of stack)
6 - def pop(self): - Method to remove and return the top item

7 - if not self.items: - Checks if stack is empty (not self.items
    means self.items is empty list)
8 - raise IndexError("Stack Underflow!") - Throws error if trying
    to pop from empty stack

9 - return self.items.pop() - Removes and returns the last element
    (LIFO - Last In First Out)
10 - return self.items[-1] if self.items else None is a ternary operator

    if self.items or if list is not empty, return the last [-1] element
    else, return None



"""

class Stack:
    def __init__(self):
        self.items = [] 

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack Underflow!")
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] if self.items else None
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Top after pop:", stack.peek())