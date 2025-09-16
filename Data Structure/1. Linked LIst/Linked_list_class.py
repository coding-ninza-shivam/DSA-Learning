class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    @staticmethod
    def print_ll(head):
        temp = head
        while temp is not None:
            print(temp.data, end='-->>')
            temp = temp.next
        print()

    @staticmethod
    def create_ll_from_list(l1):
        head=None
        tail=None
        for value in l1:
            new_node=Node(value)
            if head==Node:
                head=new_node
                tail=new_node
            else:
                tail.next=new_node
                tail=new_node
        return head

    @staticmethod
    def take_input():
        value = int(input("Enter the value of Node (-1 to stop): "))
        head = None
        tail = None
        while value != -1:
            new_node = Node(value)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            value = int(input("Enter the value of Node (-1 to stop): "))
        return head

    @staticmethod
    def length_ll(head):
        if head is None:
            return 0
        return 1 + LinkedList.length_ll(head.next)

    @staticmethod
    def insert_at_head(head):
        data = int(input("Enter the data to insert at head: "))
        new_node = Node(data)
        new_node.next = head
        return new_node

    @staticmethod
    def insert_at_tail_recursive(head, data):
        if head is None:
            return Node(data)
        head.next = LinkedList.insert_at_tail_recursive(head.next, data)
        return head

    @staticmethod
    def insert_recursion(head, data, index):
        if index == 0:
            new_node = Node(data)
            new_node.next = head
            return new_node
        if head is None:
            print("Index out of bound.")
            return head
        head.next = LinkedList.insert_recursion(head.next, data, index - 1)
        return head

    @staticmethod
    def delete_at_head(head):
        if head is None:
            return None
        return head.next

    @staticmethod
    def delete_tail(head):
        if head is None or head.next is None:
            return None
        if head.next.next is None:
            head.next = None
            return head
        head.next = LinkedList.delete_tail(head.next)
        return head

    @staticmethod
    def delete_at_index(head, index):
        if head is None:
            return None
        if index == 0:
            return head.next
        head.next = LinkedList.delete_at_index(head.next, index - 1)
        return head

    @staticmethod
    def delete_node_by_value(head, value):
        if head is None:
            print("List is empty")
            return None
        if head.data == value:
            return head.next
        temp = head
        while temp.next is not None and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("Value not found.")
            return head
        temp.next = temp.next.next
        return head

    @staticmethod
    def search_value_rec(head, value, index=0):
        if head is None:
            return "Not found"
        if head.data == value:
            return index
        return LinkedList.search_value_rec(head.next, value, index + 1)
