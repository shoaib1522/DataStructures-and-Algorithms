class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.isEmpty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            print("Stack is empty")
            return None

    def top_Func(self):
        if not self.isEmpty():
            return self.top.data
        else:
            print("Stack is empty")
            return None

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.top is None
def reverse_words(string):
        obj= Stack()
        for i in string:
            obj.push(i)
        print("OriginaL String: ",string)
        var=""
        array=[]
        for i in range(len(string)):
            object=obj.pop()
            if object == " ":
                array.append(var)
                var=''
            else:
                var+=str(object)
            if i==len(string)-1:
                array.append(var)
        last_string=""
        i=-1
        while i != (-1*len(array)-1):
                last_string+=array[i]
                last_string+=" "
                i-=1
        return(last_string)
def is_balanced(string):
    stack=Stack()
    for i in range(len(string)):
        if string[i]=='(':
            stack.push(string[i])
        elif string[i]==')':
            if stack.isEmpty():
                return False
            stack.pop()
    if stack.isEmpty():
        return True
            
stack = Stack()
print("Is stack empty?", stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.top_Func())
print("Popping:", stack.pop())
print("Top element after popping:", stack.top_Func())
print("Is stack empty?", stack.isEmpty())
print("Size of stack:", stack.size())
string="Welcome to DSA"
print('Converted String',reverse_words(string))
string='((a+b)})'
if is_balanced(string):
    print('Provided Parenthesis are good')
else:
    print('False')