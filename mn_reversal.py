# Linked List Question #7 - M, N Reversals

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
  
    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node 
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    
    def print_linkedlist(self):
        linked_list = []
        currentNode = self.head

        while currentNode != None:
            linked_list.append(currentNode.data)
            currentNode = currentNode.next 
        
        print(linked_list)
        print(f"Length of linked list: {self.length}")
        return linked_list

    def insert(self, index, data):
        new_node = Node(data)

        if index >= self.length:
            return self.append(data)
        
        if index == 0:
            return self.prepend(data)
        
        temp_node = self.traverse_index(index-1)
        new_pointer = temp_node.next
        temp_node.next = new_node
        new_node.next = new_pointer
        self.length += 1
        
    def traverse_index(self, index):
        count = 0
        currentNode = self.head

        while count != index:
            currentNode = currentNode.next
            count += 1
        
        return currentNode
    
    def remove(self, index):
        if index >= self.length:
            print("Wrong index")
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        temp_node = self.traverse_index(index-1)
        deleted_node = temp_node.next
        temp_node.next = deleted_node.next
        self.length -= 1
    
    def reverse(self):
        if self.length == 1:
            return self.head
      
        first = self.head 
        self.tail = self.head 
        second = first.next

        while second != None:
            temp = second.next 
            second.next = first 
            first = second 
            second = temp 
        
        self.head.next = None
        self.head = first

    # --- MN REVERSAL STARTS HERE --- 
    def mn_reverse(self, m, n):
        current_position = 1
        current_node = self.head
        start = self.head

        while current_position < m:
            start = current_node 
            current_node = current_node.next 
            current_position += 1
        
        new_list = None
        tail = current_node 
     
        while current_position >= m and current_position <= n:
            next_node = current_node.next
            current_node.next = new_list 
            new_list = current_node 
            current_node = next_node
            current_position += 1 
        
        start.next = new_list
        tail.next = current_node

        if m > 1:
            return self.head
        else:
            return new_list


# Testing
l = LinkedList()

print("Appending...")
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.print_linkedlist()

# Time complexity: O(n)
# Space complexity: O(1)
print("MN Reversal...")
l.mn_reverse(3, 6)
l.print_linkedlist()