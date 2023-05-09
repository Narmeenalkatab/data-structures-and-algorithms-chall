def reverseArray(arr):
    print("Input array:", arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print("Reversed array:", arr)
    return arr




assert reverseArray([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert reverseArray(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a']
assert reverseArray([1]) == [1]
assert reverseArray([]) == []