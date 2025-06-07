def fun(i):
   if (i % 2 == 1):
      i += 1
      return (i - 1)
   else:
      return fun(fun(i - 1))
print(fun(200))
