class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        """
        Inserts a new node at the beginning of the linked list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        """
        Inserts a new node at the end of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        """
        Deletes a node from the linked list with the specified value.
        """
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

    def reverse(self):
        """
        Reverses the order of nodes in the linked list.
        """
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
        """
        Displays the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" --> ")
            current = current.next
        print(None)

# Creating a Singly Linked List and testing various functions
s1 = SinglyLL()

s1.insert_at_beginning(20)
s1.insert_at_beginning(10)
s1.insert_at_end(30)
s1.display()  # Output: 10 --> 20 --> 30 --> None

s1.delete(20) # Output: 10 --> 30 --> None
s1.display()

s1.reverse() # Output: 30 --> 10 --> None
s1.display()
