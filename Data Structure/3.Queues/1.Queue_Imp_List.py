class QueueUsingLista:
    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self,element):
        self.__queue.append(element)
        return f'{element} added to queue'
    
    def front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.__queue[0]
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        removed = self.__queue.pop(0)
        return f'{removed} got dequeued.'
    
q = QueueUsingLista()
print(q.dequeue())  
print(q.isEmpty())       
print(q.enqueue(10))     
print(q.enqueue(20))     
print(q.front())  
print(q.isEmpty())           
print(q.dequeue())       
print(q.front())         
print(q.size())          