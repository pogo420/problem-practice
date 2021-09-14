
def min_window(array: list) -> int:
    unique_elemts: dict = {}
    for i in array:
        unique_elemts[i] = 1

    min_window: int = len(unique_elemts)
    window_size: int = min_window
    min_value = 100001  # variable to store minimum length

    while window_size < len(array):  # window increment
        for left in range(len(array)-window_size+1):  # sliding window
            temp: dict = {}  # temporary to save inputs
            count = 0  # counting iterations
            for i in range(left, window_size):  # traversing window
                count += 1
                if array[i] in unique_elemts:
                    temp[array[i]] = 1
                if len(temp) == len(unique_elemts):
                    if min_value > count:
                        min_value = count
        window_size += 1
    return min_value


if __name__ == '__main__':
    A = [7, 5, 2, 7, 2, 7, 4, 7]
    print(min_window(A))

    B = [2, 1, 1, 3, 2, 1, 1, 3]
    print(min_window(B))
