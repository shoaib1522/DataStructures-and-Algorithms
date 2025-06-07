def fun(n):
    if (n > 0):
        fun(n - 1)
        print(n, end=" ")
        fun(n - 1)
 # driver code
fun(4)