def counting_sort(arr):
    # Find the maximum value in the array
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    
    # Initialize count array with zeros
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Modify the count array to store the cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create the output array
    output = [0] * len(arr)
    
    # Place the elements in their correct positions in the output array
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
