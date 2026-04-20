class Node:    
    """A class to represent a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Data to store in the node
        self.next = None  # Pointer to the next node


class SingleLinkedList:    
    """A class to represent the single linked list."""
    def __init__(self):
        self.head = None  # Head of the linked list

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:       # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:# Traverse to the end of the list
            current = current.next
        current.next = new_node

  
    def display(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_length(self):
        """Return the length of the list"""
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next

        return count



    def remove_from_front(self):
        """Remove the first node and return its value"""
        if self.head is None:
            print("There is no Data in the list to remove it")
            return None
    
        removed_value = self.head.data
        self.head = self.head.next  
        return removed_value
            


    def remove_from_back(self):
        """Remove the last node and return its value"""
        #There is no value
        if self.head is None:
            print("There is no Data in the list to remove it")
            return None
        
        #There is one value
        if self.head.next is None:
            removed_value = self.head.data
            self.head = None
            return removed_value
        
        #There is more than one value
        # To delete the last node, we must change the 'next' pointer of the node before it to None. 
        # If current.next.next is None, it means current.next is the last node,
        current = self.head
        while current.next.next is not None:
            current = current.next
        #the current now is the node before the last node that we want to remove and current.next is the last element
        removed_value = current.next.data
        current.next = None  
        return removed_value
    


    def remove_val(self , val):
        """
        Remove the first node with the given value
        Args:
            val: The data value to be removed.
        """
        if self.head is None:
            return "List is empty"
        
        #the node with the given value is the first node
        if self.head.data == val:
            self.head = self.head.next
            return val
            
        current = self.head
        while current.next:
            #the node with the given value is in the last or the middle of the list
            if current.next.data == val:
                current.next = current.next.next
                return val
            current = current.next
        return f"{val} not fount in the list"



    def insert_at (self , val ,n):
        """
        Insert a node with value as the nth node in the list

        Args:
            val: The data value to be stored.
            n: The index position where the node should be inserted.
        """
        length = self.get_length()
        if n<0 or n>length:
            return "Index out of bounds"

        if n==0:
            self.insert_at_beginning(val)
            return
        
        if n == length:
            self.insert_at_end(val)
            return
        
        count = 0
        current = self.head
        while current:
            if count == n -1:
                new_node = Node(val)
                new_node.next = current.next
                current.next = new_node
                return
            
            current = current.next
            count +=1


# Example usage
linked_list = SingleLinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_end(30)
linked_list.display() # Output: 20 -> 10 -> 30 -> None

linked_list.remove_val(10)
linked_list.display() # Output: 20 -> 30 -> None

linked_list.remove_from_front()
linked_list.display() # Output: 30 -> None

linked_list.remove_from_back()
linked_list.display() # Output: None

linked_list.insert_at(15, 0) 
linked_list.insert_at(10, 1) 
linked_list.display() # Output: 15 -> 10 -> None

linked_list.remove_val(15) 
linked_list.display()# Output: 10 -> None

print("Length of list:", linked_list.get_length())