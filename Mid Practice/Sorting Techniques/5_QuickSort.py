def partition(a, p, q, r):
    pivot = a[q]
    i = p - 1
    for j in range(p, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[q] = a[q], a[i + 1]
    return i + 1
def Quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, (p + r) // 2, r)
        print(q, p, (p + r) // 2, r)
        Quick_sort(a, p, q - 1)
        Quick_sort(a, q + 1, r)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
Quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
