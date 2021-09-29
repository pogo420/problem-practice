
def insert(arr, tmp):
    if len(arr) == 0 or arr[len(arr)-1] < tmp:
        arr.append(tmp)
        return arr
    val = arr.pop()   # remove last element
    arr = insert(arr, tmp)  # do recursive call
    arr.append(val)  # push the value
    return arr


def sort_(array: list):
    if len(array) == 1:  # single element is sorted
        return array

    temp = array.pop()   # reduce element
    array = sort_(array)  # call the function
    array = insert(array, temp)
    return array


if __name__ == '__main__':
    d = [6, 1, 8, 2, 4]
    print(sort_(d))
