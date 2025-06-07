def is_palindrome(string):
    start,end=0,-1
    if len(string)==0 or len(string)==1:
        return True
    if string[start]==string[end]:
        return is_palindrome(string[1:-1])
    return False
def main(): 
    array_strings=["racecar","tesla","radar","level","elephant"]
    for element in array_strings:
        if is_palindrome(element):
            print(f'Yes, the "{element}" is a palindrome')
        else:
            print(f'No, the "{element}" is not a palindrome ')
main()
