
def search(arr, l, h, key):
    if l > h:  # check for not found cases
        return -1

    mid = (l+h)//2  # calculating mid

    if arr[mid] == key:  # matching in mid
        return mid

    if arr[l] <= arr[mid] :   # checking if left is sorted
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid, key)
        return search(arr, mid+1, h, key)

    if key >= arr[mid+1] and key < arr[h]:
        return search(arr, mid+1, h, key)
    return search(arr, l, mid, key)


ar = [3,4,5,1,2]
print(search(ar, 0, 4, 10))
