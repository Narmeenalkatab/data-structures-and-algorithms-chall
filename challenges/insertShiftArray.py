def insertShiftArray(arr, val):
    n = len(arr)
    mid = (n + 1) // 2
    arr.append(val)
    for i in range(mid, n+1):
        arr[n-i+mid] = arr[n-i+mid-1]
    arr[mid] = val
    return arr




print(insertShiftArray([2, 4, 6, -8], 5))  # expected output: [2, 4, 5, 6, -8]
# expected output: [42, 8, 15, 16, 23, 42]
print(insertShiftArray([42, 8, 15, 23, 42], 16))
