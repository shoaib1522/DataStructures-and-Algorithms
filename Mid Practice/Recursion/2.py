def recursive_fact(n):
    if n==0:
        return 1
    else:
       return n*recursive_fact(n-1)
print('2! = ',recursive_fact(2))
print('3! = ',recursive_fact(3))
print('4! = ',recursive_fact(4))
print('5! = ',recursive_fact(5))
print('6! = ',recursive_fact(6))