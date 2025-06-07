def print_recursive(n,i=1):
    if n <= 0:
        return
    else:
        print(f"{n}-Hello World")
        print_recursive(n - 1,i+1)
def print_recursive2(n):
    if n <= 0:
        return
    else:
        print_recursive2(n - 1)
        print(f"{n}-Hello World")

def main():
    print_recursive(5)
    print('--------------')
    print_recursive2(15)

if __name__ == "__main__":
    main()
