# which element is present more than N//2 times.


def moores_majority_algorithm(array: list):
    tracker = [0, 0]
    for i in array:
        if tracker[0] == i and tracker[1] > 0:  # if element is matching and count is > 0 it can be a majority
            tracker[1] += 1
        elif tracker[0] != i and tracker[1] > 0:  # if prev element is not matching and count is > 0
                                                  # it can be a majority but will reduce count
            tracker[1] -= 1
        else:  # count is 0 , lets pic new element
            tracker[0] = i
            tracker[1] += 1

    # Its guaranteed majority element's count will be > 0 at the end
    if tracker[1] > 0:
        return True, tracker[0]
    else:
        return False, tracker[1]


if __name__ == '__main__':
    a = [5, 1, 4, 1, 1]
    print(moores_majority_algorithm(a))

    a = [5, 1, 5, 1, 5]
    print(moores_majority_algorithm(a))
