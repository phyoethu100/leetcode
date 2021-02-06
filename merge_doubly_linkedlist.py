# Linked List Question #8 - Merge Multi-Level Doubly Linked List

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()


    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node 
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
            self.length += 1
            return


    def insert(self, position, data):
        if position == 0:
            self.prepend(data) 
            return
        if position >= self.length:
            self.append(data) 
            return
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position - 1): 
                current_node = current_node.next
            new_node.prev = current_node 
            new_node.next = current_node.next 
            current_node.next = new_node 
            new_node.next.prev = new_node 
            self.length += 1
            return


    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None: 
                self.tail = self.head
            if self.head != None:
                self.head.prev = None 
            self.length -= 1
            return
        try: 
            while current_node!= None and current_node.next.data != data:
                current_node = current_node.next
            if current_node!=None:
                current_node.next = current_node.next.next
                if current_node.next != None: 
                    current_node.next.prev = current_node 
                else:
                    self.tail = current_node 
                self.length -= 1
                return
        except AttributeError:
            print("Given value not found.")
            return


    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            if self.head != None:
                self.head.prev = None 
            self.length -= 1
            return

        if position>=self.length:
            position = self.length-1

        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next != None: 
            current_node.next.prev = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return
    
    def merge_double_linkedlist(self):
        if self.head == None:
            return self.head
        
        current_node = self.head

        while current_node != None:
            if current_node.child == None:
                current_node = current_node.next
            else:
                self.tail = current_node.child
                while self.tail.next != None:
                    self.tail = tail.next
                self.tail.next = current_node.next
                if self.tail.next != None:
                    self.tail.next.prev = self.tail
                current_node.next = current_node.child
                current_node.prev = current_node
                current_node.child = None

# Testing
l = DoublyLinkedList()

l.append(5)
l.append(2)
l.append(9)
l.print_list()

# Time complexity: O(n)
# Space complexity: O(1)