# brute force - n^2 using two loops.
# kadence's algorithms: O(n) complexity.


def largest_subarray(array):
    max_sum = 0
    curr_sum = 0
    for i in array:
        curr_sum += i
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:  # when current sum is <0 reinitialize. Keeping prev elements will reduce the sum
            curr_sum = 0
    return max_sum


if __name__ == '__main__':
    a = [-5, 4, 6, -3, 4, -1]
    print(largest_subarray(a))
