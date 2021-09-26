# each pass max (asc) or min(desc) goes to the end of list, like bubble
# we swap elements for n passes and each pass we compare n items so , O(n^2).
# bubble can be used if we need to find.
# after ith iteration , we will get i elements bubble out of unsorted list in sorted order.

def bubble(data_):
    i = 0
    while i < len(data_):  # each pass
        print(data_)
        j = 0
        swapped = False
        while j < len(data_) - 1 - i:  # swapping in each pass, no need to go till end as we have sorted stuff at end.
            if data_[j] > data_[j + 1]:
                swapped = True
                data_[j] = data_[j] ^ data_[j + 1]
                data_[j + 1] = data_[j] ^ data_[j + 1]
                data_[j] = data_[j] ^ data_[j + 1]
            j += 1
        if not swapped:  # already sorted return in few passes
            break
        i += 1


if __name__ == '__main__':
    data = [4, 3, 7, 1, 5]
    bubble(data)
    print(data)
