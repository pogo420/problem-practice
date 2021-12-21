
def get_floor(array, key):
    # function to calculate the floor data

    start = 0
    end = len(array) - 1
    result = -1
    while start <= end:
        print(start, end)
        mid = start + ((end - start )//2)
        if key == array[mid]:
            result = key
            break

        if key > array[mid]:
            result = array[mid]
            end = mid - 1

        if key < array[mid]:
            start = mid + 1

    return result


if __name__ == '__main__':
    b = [100, 90, 90, 70, 60]
    index = get_floor(b, 100)
    print(index)