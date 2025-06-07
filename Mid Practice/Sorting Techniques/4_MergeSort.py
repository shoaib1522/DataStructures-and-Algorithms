def merge_sort(arr):
    def merge(arr, p, q, r):
        # Merge two sorted subarrays arr[p..q] and arr[q+1..r]
        n1 = q - p + 1
        n2 = r - q

        # Create temporary arrays to hold the subarrays
        L = arr[p:p + n1]
        R = arr[q + 1:q + 1 + n2]

        # Merge the temporary arrays back into arr[p..r]
        i = j = 0
        k = p
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L (if any)
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R (if any)
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(arr, p, r):
        if p < r:
            # Find the middle index
            q = (p + r) // 2

            # Recursively sort the two halves
            print(p,'  ',q)
            merge_sort(arr, p, q)
            print('-------------')
            print(q+1,' ',r)
            merge_sort(arr, q + 1, r)

            # Merge the sorted halves
            print('call',p,q,r)
            merge(arr, p, q, r)

    merge_sort(arr, 0, len(arr) - 1)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Sorted array:", arr)
