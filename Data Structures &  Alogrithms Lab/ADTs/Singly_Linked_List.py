class Node:
    def __init__(self, info=None):
        self.info = info
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, info):
        new_node = Node(info)
        if self.head is None: 
            self.head = new_node 
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, info):
        new_node = Node(info)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_after(self, prev_info, info):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            if temp.info == prev_info:
                new_node = Node(info)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"{prev_info} not found in the list")

    def insert_before(self, next_info, info):
        if self.head is None:
            print("List is empty")
            return
        if self.head.info == next_info:
            self.insert_at_head(info)
            return
        temp = self.head
        while temp.next:
            if temp.next.info == next_info:
                new_node = Node(info)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"{next_info} not found in the list")

    def display(self):
        temp = self.head
        while temp:
            print(temp.info, end=" -> ")
            temp = temp.next
        print("None")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.info == key:
                return True
            temp = temp.next
        return False

    def update(self, old_val, new_val):
        temp = self.head
        while temp:
            if temp.info == old_val:
                temp.info = new_val
                return
            temp = temp.next
        print(f"{old_val} not found in the list")

    def remove_at_head(self):
        if self.head:
            self.head = self.head.next

    def remove_at_tail(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def remove_after(self, prev_info):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            if temp.info == prev_info:
                if temp.next:
                    temp.next = temp.next.next
                    return
                else:
                    print(f"No node after {prev_info}")
                    return
            temp = temp.next
        print(f"{prev_info} not found in the list")

    def remove_before(self, next_info):
        if self.head is None:
            print("List is empty")
            return
        if self.head.info == next_info:
            print("No node before the head")
            return
        if self.head.next.info == next_info:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next.next:
            if temp.next.next.info == next_info:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"{next_info} not found in the list")

# Example usage:
if __name__ == "__main__":
    # Create a singly linked list
    linked_list = SinglyLinkedList()
    
    # Insert at head
    linked_list.insert_at_head(1)
    linked_list.insert_at_head(0)
    
    # Insert at tail
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    
    # Insert after an element
    linked_list.insert_after(2, 2.5)
    
    # Insert before an element
    linked_list.insert_before(3, 2.75)
    
    # Display the list
    linked_list.display()  # Output: 0 -> 1 -> 2 -> 2.5 -> 2.75 -> 3 -> None
    
    # Search for an element
    print(linked_list.search(2.5))  # Output: True
    print(linked_list.search(5))    # Output: False
    
    # Update an element
    linked_list.update(2.75, 2.8)
    linked_list.display()  # Output: 0 -> 1 -> 2 -> 2.5 -> 2.8 -> 3 -> None
    
    # Remove elements
    linked_list.remove_at_head()
    linked_list.remove_at_tail()
    linked_list.remove_after(1)
    linked_list.remove_before(2)
    
    # Display the list after removals
    linked_list.display()  # Output: 0 -> 1 -> 2.5 -> None
