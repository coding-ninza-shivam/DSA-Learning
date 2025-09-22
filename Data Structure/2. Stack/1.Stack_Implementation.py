'''
Stack implementation using inbulid python list
'''

class StackUsingList:
    def __init__(self):
        self.__stack = []

    def push(self,data):
        self.__stack.append(data)
        print(f"Pushed {data} into stack.")
    
    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        return len(self.__stack)==0
    
    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.__stack[-1]
    
    def pop(self):
        return self.__stack.pop()


my_stack = StackUsingList()
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