def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quicksort(arr, l, p - 1)
        quicksort(arr, p + 1, l)


def partition(arr, l, r):
    p = arr[r]
    i = l - 1

    for j in range(r):
        if arr[j] <= p:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1

    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp

    return i + 1

arr = [3, 4, 5, 8, 9, 7]
quicksort(arr, 0, len(arr) - 1)
print arr
