def reverse_string(string):
    if len(string)==0 or len(string)==1:
        return string
    return f"{string[-1]}{reverse_string(string[0:-1])}"
def main():
    strings=["Tesla","Norma","Lebinis","Elephant"]
    for string in strings:
        print(f'The reverse string of "{string}" is : {reverse_string(string)}')
main()