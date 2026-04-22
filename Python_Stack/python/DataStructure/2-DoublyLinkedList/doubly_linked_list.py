# Add a new node to the end of the list,
# delete an existing node,
# and insert a node between existing nodes (e.g., before a given value, at a particular index, etc.)
# You should have two classes for this: DoublyLinkedList and Node. 
# DoublyLinkedList should be the class that allows you to add a new node, delete an existing node, 
# insert a new node between existing nodes, and print out the values in the linked list. 


# How would you know if you have a circular linked list?
# How would you get to the middle of the linked list?
# How would you remove duplicate values from the list?
# How would you reverse the values in the list?
class Node:
    def __init__(self, data):        
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the end of the DLL
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Forward traversal (head to tail)
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    # Backward traversal (tail to head)
    def traverse_backward(self):
        temp = self.head
        if not temp:
            print("List is empty!")
            return
        # Move to the tail of the list
        while temp.next:
            temp = temp.next
        # Traverse backward from tail to head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)


print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()