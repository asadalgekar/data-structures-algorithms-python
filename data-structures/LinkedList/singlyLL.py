class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SinglyLL:
    
    def __init__(self):
        self.head = None
        
    def insert_node_begining(self, value):
        """Insert a node at the beginning of the linked list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insert_node_end(self, value):
        """Insert a node at the end of the linked list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def delete(self, key):
        """Delete the node with the specified value from the linked list."""
        if not self.head:
            return
        if self.head.value == key:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current and current.value != key:
            previous = current
            current = current.next
        if not current:
            return
        else:
            previous.next = current.next
                
    def length(self):
        """Calculate and display the length of the linked list."""
        count = 0 
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Length of SinglyLL: {count}")
    
    def reverse(self):
        """Reverse the linked list in-place."""
        if not self.head or not self.head.next:
            return
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
            
    def display(self):
        """Display the values of nodes in the linked list."""
        current = self.head
        while current:
            print(current.value , end=" --> ")
            current = current.next
        print(None)
        
s1 = SinglyLL()
s1.insert_node_begining(20)
s1.insert_node_begining(10)
s1.insert_node_end(30)
s1.insert_node_end(40)

s1.delete(40)
s1.display()  # Output: 10 --> 20 --> 30 --> None

s1.length()   # Output: Length of SinglyLL: 3

s1.reverse()  # Output: 30 --> 20 --> 10 --> None
