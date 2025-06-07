def dec2oct(n):
    if n<8:
        return n%8
    return f"{dec2oct(n//8)}{n%8}"
def main():
    obj=[16,20,13]
    for object in obj:
        print(f"The Octal Number Equivalent to {object} is : {dec2oct(object)}")
main()