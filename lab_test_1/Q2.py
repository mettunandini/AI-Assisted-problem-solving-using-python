#You are an AI coding assistant. Write Python code for data structures.

#Example 1:
#Task: Create a stack with push and pop methods.
#Code:
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

#Example 2:
#Task: Create a queue with enqueue and dequeue methods.
#Code:
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

#Now your task:
#Task: Create a basic linked list with methods to insert a node at the end and delete a node by value.
#Code:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return  # Key not found
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        return elems

# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Before deletion:", ll.display())
ll.delete(20)
print("After deletion:", ll.display())
