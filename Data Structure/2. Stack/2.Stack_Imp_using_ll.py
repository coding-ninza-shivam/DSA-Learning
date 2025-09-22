class Node:
    def __init__(self,data):
         self.data = data
         self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def push(self,data):
            newNode = Node(data)
            self.length+=1 
            if self.head is None:
                self.head = newNode
                return f"Added {data} to the stack."
            newNode.next = self.head
            self.head = newNode
            return f"Added {data} to the stack."

    def top(self):
            if self.head is None or self.size == 0:
                return 'Stack is empty.'
            return self.head.data
    
    def pop(self):
        if self.head is None or self.size == 0:
                return 'Stack is empty.'
        data_at_top = self.head.data
        self.head = self.head.next
        self.length-=1
        return data_at_top
    
    def size(self):
         return self.length
    
    def is_empty(self):
        return self.length == 0
    
my_stack = StackUsingLinkedList()
print(my_stack.is_empty())
print(my_stack.push(1)) 
print(my_stack.push(2)) 
print(my_stack.push(3)) 
print(my_stack.push(4)) 
print(my_stack.is_empty()) 
print(my_stack.pop()) 
print(my_stack.pop()) 
print(my_stack.is_empty()) 
print(my_stack.size()) 
print(my_stack.top())