def array_sum_recursive(arr, n):
  # Base case: If n is 0, the sum is 0
  if n == 0:
    return 0

  # Recursive case: Add the first element of the array and sum the remaining elements (n-1)
  else:
    print(arr) # ---> Its a actual Point in it
    return arr[0] + array_sum_recursive(arr[1:], n-1)
def array_sum_recursive2(arr, n):

  if n == 0:
    return 0
  else:
    return array_sum_recursive2(arr, n-1) + arr[n-1]


# Example usage
my_array = [1, 2, 3, 4, 5]
n = 3
result = array_sum_recursive2(my_array, n)
print(f"The sum of the first {n} integers in the array is: {result}")
