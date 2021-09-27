# only unsorted list, we select min/max from the list and swap it to first element of unsorted list.
# next iteration: we select min/max from the list(second to end) and swap it to second element of unsorted list.
# with each iteration sorted list increases and unsorted decreases.
# Difference with insertion sort? Here we append at the end of sorted part.
# In insertion we insert among the elements of sorted arrary

# use case: sort first few elements of an array, swaps are less as compared to bubble.


def insertion(data):
    for i in range(len(data)):  # with i increasing, sorted increases(0-n) unsorted decreases(n-0)
        j = i
        mix_ = 100000
        min_index = 0
        while j < len(data):  # calculating the minimum value
            if mix_ > data[j]:
                mix_ = data[j]
                min_index = j
            j += 1

        if data[i] > data[min_index] and i != min_index:  # swapping the unsorted start with min/max value
            data[i] = data[i] ^ data[min_index]
            data[min_index] = data[i] ^ data[min_index]
            data[i] = data[i] ^ data[min_index]

    return data


if __name__ == '__main__':
    data = [4, 3, 7, 1, 5]
    insertion(data)
    print(data)
