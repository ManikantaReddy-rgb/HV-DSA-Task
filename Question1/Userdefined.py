def check_ele(arr, n, ele):
    count = 0
    for i in range(n):
        if arr[i] == ele:
            count += 1
    return count

def find_dup(arr, n):
    for i in range(n):
        count = check_ele(arr, n, arr[i])
        if count > 1:
            print("The frequency of", arr[i], "is:", count)

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
n = len(arr)
find_dup(arr, n)
