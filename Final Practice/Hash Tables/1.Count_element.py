def count_elements(array):
    # Using a dictionary to count the occurrences of each element
    counts = {}
    for element in array:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# Example usage
array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = count_elements(array)
print(counts)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}
