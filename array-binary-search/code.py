''' create function called binary_search that
    takes two arguments arr and target '''
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 # as length of array -1 so (length array = low + high)

    while low <= high:
        mid = (low + high) // 2 #as reference point
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__=="__main__":
    arr = ['A','B','C']
    target = 'A'
    result= binary_search(arr,target)
    print (result)
   