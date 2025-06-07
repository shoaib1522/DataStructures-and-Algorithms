n = int(input('Enter the term of Fibonacci You wanna get : '))
a, b = 0, 1
for i in range(n):
 c = a +b
 a = b
 b = c
print(a)