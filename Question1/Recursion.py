def dup_ele(arr, n, freq, ele):
    if n == 0:
        return
    if arr[n-1] == ele:
        freq[0] += 1
    dup_ele(arr, n-1, freq, ele)

def find_dup(arr, n):
    for i in range(n):
        freq = [0]
        dup_ele(arr, n, freq, arr[i])
        if freq[0] > 1:
            print("The frequency of", arr[i], "is:", freq[0])

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
n = len(arr)
find_dup(arr, n)
