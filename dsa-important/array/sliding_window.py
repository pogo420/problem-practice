
def sliding_window(arr, k):
    i = 0
    j = 0
    result = []  # result
    temp = []  # temp data

    max_ = - 1000

    while j < len(arr):

        temp.append(arr[j])
        max_ = max(max_, arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            result.append(max_)
            temp = temp[1:]  # reducing first element
            if max_ == arr[i]:  # calculating mix from remaining element if first element is max
                max_ = max(temp)  # modifying the max data
            j += 1
            i += 1

    return result


if __name__ == '__main__':
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
    print(sliding_window(A, B))