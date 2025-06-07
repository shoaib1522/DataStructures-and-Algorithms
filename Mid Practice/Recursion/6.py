def fun(a, n):
    if (n == 1):
        return a[0]
    else:
        x = fun(a, n - 1)
    if (x > a[n - 1]):
        return x
    else:
        return a[n - 1]
# Driver code
arr = [15,18,8,6,2]
print(fun(arr, 5))
# arr = [12, 1, 30, 5, 10]
# print(fun(arr, 5))