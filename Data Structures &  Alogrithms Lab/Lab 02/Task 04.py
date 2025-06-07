class Node: 
    def __init__(self, val=None): 
        self.info = val 
        self.next = None 
 
class LinkList: 
    def __init__(self): 
        self.head = None 
    def insert_at_head(self, val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
    def insert_at_tail(self, val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def insert_after(self, key, val):
        new_node = Node(val)
        temp = self.head
        while temp:
            if temp.info == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"Key '{key}' not found in the linked list.")

    def insert_before(self, key, val):
        new_node = Node(val)
        if not self.head:
            print("Linked list is empty.")
            return
        if self.head.info == key:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            if temp.next.info == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"Key '{key}' not found in the linked list.")
    def search(self, key):
        temp = self.head
        i = 1
        while temp:
            if temp.info == key:
                return i
            current = current.next
            i += 1
        return -1 
    def display(self):
        temp = self.head
        while temp:
            print(temp.info, end=" ")
            temp = temp.next
        print()
if __name__ == "__main__": 
    obj = LinkList() 
    obj.insert_at_head(2) 
    obj.insert_at_head(3) 
    obj.insert_at_tail(9) 
    obj.insert_after(3,4) 
    obj.insert_before(9,8) 
 
    obj.display()