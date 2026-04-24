class Node:
    def __init__(self, data):        
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    #1. Insert at Head
    def insert_at_beginning(self , val):
        new_node = Node(val)
        if self.head is None: # If the list is empty
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    #2. Insert at the end
    def append(self , val):
        new_node = Node(val)
        if self.head is None: # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            new_node.prev = current
            current.next = new_node

    #3. Insert a node between existing nodes (before a given value)
    def insert_before_value(self, target_val, value):
        if self.head is None:
            return "List is empty"

        current = self.head
        while current:
            if current.data == target_val:
                new_node = Node(value)
                new_node.next = current
                new_node.prev = current.prev
                
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                
                current.prev = new_node
                return
            
            current = current.next
        return "Value Not Found"

    #4. Insert a node between existing nodes (at a particular index)
    def insert_at_index(self ,value , index):
        if index == 0 :
            self.insert_at_beginning(value)
            return
        
        count = 0
        current = self.head
        new_node = Node(value)
        while current :
            if count ==  index - 1:
                if current.next is not None:
                    current.next.prev  = new_node

                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                return
                        
            count +=1
            current = current.next
        return "Index Not Found"
                          
    #5. Delete an existing node
    def remove_val(self, val):
        if self.head is None:
            return "List is empty"

        current = self.head
        while current:
            if current.data == val:
                if current == self.head:
                    self.head = current.next
                    if self.head: 
                        self.head.prev = None
                    return val
                
                if current.next: 
                    current.next.prev = current.prev
                
                if current.prev: 
                    current.prev.next = current.next
                
                return val
            current = current.next
        
        return "Value not found"

    # Forward traversal (head to tail)
    def traverse_forward(self):
        current = self.head
        while current:
            print (f"{current.data}", "-> ")
            current = current.next
        print("None")

    # Backward traversal (tail to head)
    def traverse_backward(self):
        current = self.head
        if current is None:
            print("List is empty!")
            return
        # Move to the end of the list
        while current.next:
            current = current.next
        # Traverse backward from end to head
        while current:
            print (f"{current.data}", "-> ")
            current = current.prev
        print("None")

    #reverse the values in the list
    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp

            current = current.prev
        
        if temp:
            self.head = temp.prev


# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(5)
dll.insert_at_beginning(0)
dll.append(10)
dll.append(20)
dll.append(30)
dll.insert_at_index(15,3)
dll.insert_before_value(30,25)

dll.remove_val(10)
#dll.reverse()

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()


# How would you get to the middle of the linked list?
# How would you remove duplicate values from the list?