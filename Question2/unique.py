def unique_elements(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [5, 4, 7, 5, 1, 3, 4]
arr = unique_elements(arr)
arr = sort_array(arr)

print(arr)
