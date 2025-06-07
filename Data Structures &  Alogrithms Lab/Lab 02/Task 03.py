def is_GoodString(String , index=0):
    if index == len(String):
        return True
    digit = int(String[index])
    if (index % 2 == 0 and digit % 2 == 0) or (index % 2 == 1 and is_prime(digit)):
        return is_GoodString(String, index + 1)
    else:
        return False
def is_prime(n):
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True
def main():
    
    strings=["02468","23478"]
    for string in strings:
        if is_GoodString(string):
            print(f"The Given String '{string}' is a Good String")
        else:
            print(f"The Given String '{string}' is not a Good String")
main()
