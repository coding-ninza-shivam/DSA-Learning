"""
Queue implementation using linked list
"""

class Node:
    def __init__(self,data):
         self.data = data
         self.next = None 

class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def size(self):
        return self.len
    
    def isEmp(self):
        return self.size() == 0
    
    def enque(self,data):
        newNode = Node(data)
        self.len+=1 
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return f"Added {data} to the queue."
        else:
            self.next.tail = newNode
            self.tail = newNode
            return f"Added {data} to the queue."
        
    def front(self):
        if self.head is None:
            return "Queue is empty"
        return self.head.data
    
    def dequeue(self):
        if self.isEmp():
            return "Queue is empty"
        self.len-=1
        dequeued_data = self.head.data
        self.head = self.head.next 
        if self.head is None: # Very important to handle the right form  for further implementations
            self.tail = None
        return f"{dequeued_data} is dequeued from the queue"

q = QueueUsingLinkedList()
print(q.dequeue())  
print(q.isEmpty())       
print(q.enqueue(10))     
print(q.enqueue(20))     
print(q.front())  
print(q.isEmpty())           
print(q.dequeue())       
print(q.front())         
print(q.size())          