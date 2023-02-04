def find_dup(arr, n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > 1:
            print("The frequency of", arr[i], "is:", count)

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
n = len(arr)
find_dup(arr, n)
