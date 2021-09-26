# We have two part of list, sorted and unsorted.
# every iteration we place an element from unsorted list to sorted list.
# Summary, after ith iteration first i elements of the list will be sorted.
# perfect use case, when we need to add unsorted data(small) in a large sorted data.


def insertion(data):
    i = 1
    while i < len(data):
        key = data[i]  # key, starting point of unsorted array.

        j = i - 1
        while j >= 0 and key <= data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key  # inserting into appropiate location
        i += 1
    return data


if __name__ == '__main__':
    data = [4, 3, 7, 1, 5]
    insertion(data)
    print(data)
