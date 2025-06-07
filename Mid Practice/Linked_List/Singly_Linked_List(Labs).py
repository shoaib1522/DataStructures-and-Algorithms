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
        
    def remove(self, val):
        if self.head is None:
            print("List is empty")
            return
        if self.head.info == val:
            print("No node before the head")
            return
        if self.head.next and self.head.next.info == val:
            self.head.next = self.head.next.next
            return
        temp = self.head
        while temp.next:
            if temp.next.info == val:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"{val} not found in the list")    
# __________________Labs Answers____________________________
    def remove_kth_Node(self,k):
        if self.head is None:
            print("List is empty")
            return False
        if k ==1:
            self.head = self.head.next
            return True
        count = 1
        temp = self.head
        while temp and count <= k-1 :
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            print("K is greater")
            return False
        temp.next = temp.next.next
        return True
    
    def combine(self, list1, list2):
        if list1.head is None:
            self.head = list2.head
            list2.head = None
            return
        self.head = list1.head
        temp = list1.head
        while temp.next:
            temp = temp.next
        temp.next = list2.head
        list1.head = None
        list2.head = None
    def shuffleMerge(self, list1, list2):
        if list1.head is None:
            self.head = list2.head
            list2.head = None
            return
        temp1 = list1.head
        temp2 = list2.head
        isOn=True
        while temp1 and temp2:
            if isOn==True:
                self.insert_at_tail(temp1.info)
                temp1=temp1.next
                isOn=False
            else:
                self.insert_at_tail(temp2.info)
                temp2 = temp2.next
                isOn=True
        list1.head = None
        list2.head = None
    def removeDuplicates(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            temp1 = temp
            while temp1.next:
                if temp1.next.info == temp.info:
                    temp1.next = temp1.next.next
                else:
                    temp1 = temp1.next
            temp = temp.next
    def reverseList(self):
        if self.head is None or self.head.next is None:
            return
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    def reverseList2(self):
        def _reverse_recursive(current, prev):
            if current is None:
                self.head = prev
                return
            next_node = current.next
            current.next = prev
            _reverse_recursive(next_node, current)

        if self.head is None or self.head.next is None:
            return
        _reverse_recursive(self.head, None)
    def has_loop(head):
        if head is None:
            return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Example usage:
if __name__ == "__main__":
    # Create a singly linked list
    linked_list = SinglyLinkedList()
    
    # Insert elements
    linked_list.insert_at_head(4)
    linked_list.insert_at_head(2)
    linked_list.insert_at_tail(8)
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(9)
    linked_list.insert_at_tail(5)
    linked_list.insert_at_tail(4)
    linked_list.insert_at_tail(6)
    
    # Display the list
    linked_list.display()  # Output: 4 -> 2 -> 8 -> 1 -> 9 -> 5 -> 4 -> 6 -> None
    
    # Remove Kth node
    linked_list.removeKthNode(4)
    linked_list.display()  # Output: 4 -> 2 -> 8 -> 9 -> 5 -> 4 -> 6 -> None

    # Create two more linked lists
    list1 = SinglyLinkedList()
    list1.insert_at_tail(7)
    list1.insert_at_tail(3)
    list1.insert_at_tail(4)
    list1.insert_at_tail(2)

    list2 = SinglyLinkedList()
    list2.insert_at_tail(5)
    list2.insert_at_tail(9)

    # Combine lists
    list3 = SinglyLinkedList()
    list3.combine(list1, list2)
    list3.display()  # Output: 7 -> 3 -> 4 -> 2 -> 5 -> 9 -> None

    # Shuffle merge lists
    list4 = SinglyLinkedList()
    list4.shuffleMerge(list1, list2)
    list4.display()  # Output: 7 -> 5 -> 3 -> 9 -> 4 -> None

    # Remove duplicates
    list4.removeDuplicates()
    list4.display()  # Output: 7 -> 5 -> 3 -> 9 -> 4 -> None

    # Reverse list
    list4.reverseList()
    list4.display()  # Output: 4 -> 9 -> 3 -> 5 -> 7 -> None
