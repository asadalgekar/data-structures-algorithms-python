class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value):
        """
        Inserts a new node at the beginning of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, value):
        """
        Inserts a new node at the end of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, key):
        """
        Deletes a node from the linked list with the specified value.
        """
        if not self.head:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        if self.head.value == key:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        if self.tail.value == key:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        current = self.head.next
        while current and current.next:
            if current.value == key:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

    def reverse(self):
        """
        Reverses the order of nodes in the linked list.
        """
        if not self.head or not self.head.next:
            return
        
        current = self.head
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            current = next_node
        self.head, self.tail = self.tail, self.head

    def display(self):
        """
        Displays the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" --> ")
            current = current.next
        print(None)

# Creating a Doubly Linked List and testing various functions
d1 = DoublyLL()

d1.insert_at_beginning(20)
d1.insert_at_beginning(10)
d1.insert_at_end(30)
d1.display()  # Output: 10 --> 20 --> 30 --> None

d1.delete(20) # Output: 10 --> 30 --> None
d1.display()

d1.reverse() # Output: 30 --> 10 --> None
d1.display()
