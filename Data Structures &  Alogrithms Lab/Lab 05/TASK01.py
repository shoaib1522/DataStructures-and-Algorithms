def precedence(operater):
    if operater=="+" or operater=="-":
        return 1
    if operater=="*" or operater=="/":
        return 2
    else:
        return 0
def convert(string):
    stack=[]
    ITEMS =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string_out=""
    for item in string:
        if item in ITEMS:
            string_out+=(item)
        elif item =='(':
            stack.append(item)
        elif item == ')':
            while stack and stack[-1] != '(':
                string_out += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(item):
                string_out+=stack.pop()
            stack.append(item)
    while stack:
        string_out+=stack.pop()
    return string_out
def task02(string):
    new_string=""
    for i in range(len(string)):
        if string[-i]=="(":
            new_string+=')'
        elif string[-i]==")":
            new_string+='('
        else:
            new_string+=string[-i]
    # converted=convert(new_string)
    print(new_string)
    # for i in range(len(converted)):
    #     if converted[]
        
            
s="(4+8)*(6-5)/((3-2)*(2+2))"
print(convert(s))
task02(s)
        
            
