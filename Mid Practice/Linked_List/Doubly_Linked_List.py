class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, prev_data, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return
            current = current.next

        print(f"{prev_data} not found in the list")

    def insert_before(self, next_data, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current:
            if current.data == next_data:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                return
            current = current.next

        print(f"{next_data} not found in the list")

    def delete_at_head(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_tail(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_by_value(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.delete_at_head()
            return

        current = self.head
        while current:
            if current.data == data:
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                current.prev.next = current.next
                return
            current = current.next

        print(f"{data} not found in the list")

    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_at_head()
            return

        current = self.head
        count = 1
        while current:
            if count == position:
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                current.prev.next = current.next
                return
            current = current.next
            count += 1

        print(f"Invalid position: {position}")

    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def search(self, data):
        if self.head is None:
            return False

        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def update(self, old_data, new_data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

        print(f"{old_data} not found in the list")

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def is_empty(self):
        return self.head is None

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

# Example usage:
if __name__ == "__main__":
    # Create a doubly linked list
    dll = DoublyLinkedList()

    # Insert elements
    dll.insert_at_head(1)
    dll.insert_at_head(0)
    dll.insert_at_tail(2)
    dll.insert_at_tail(3)

    # Display the list forward
    print("Forward:")
    dll.display_forward()  # Output: 0 -> 1 -> 2 -> 3 -> None

    # Display the list backward
    print("Backward:")
    dll.display_backward()  # Output: 3 -> 2 -> 1 -> 0 -> None

    # Delete elements
    dll.delete_at_head()
    dll.delete_at_tail()
    dll.delete_by_value(1)
    dll.delete_by_position(2)

    # Display the list forward after deletion
    print("Forward after deletion:")
    dll.display_forward()  # Output: 2 -> None

    # Search for an element
    print("Search:")
    print(dll.search(2))  # Output: True
    print(dll.search(3))  # Output: False

    # Update an element
    dll.update(2, 5)
    dll.display_forward()  # Output: 5 -> None

    # Get length of the list
    print("Length:", dll.get_length())  # Output: 1

    # Check if the list is empty
    print("Is empty:", dll.is_empty())  # Output: False

    # Reverse the list
    dll.reverse()
    dll.display_forward()  # Output: 5 -> None
    dll.display_backward()  # Output: 5 -> None
