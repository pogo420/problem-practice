

def remove_duplicates(array, duplicates):
    # constant space, modifying the same array
    j = 0  # modifying the same array
    for i in range(len(array) - duplicates):
        if array[i] != array[i + duplicates]:
            array[j] = array[i]
            j += 1

    # back fill logic
    fill_up = duplicates
    while fill_up > 0:
        array[j] = array[len(array) - fill_up]  # back fill elements missed due to for
        j += 1
        fill_up -= 1
    print(f"{j} elements are duplicates of {duplicates}")


if __name__ == '__main__':
    a = [0, 0, 1, 1, 1, 1, 2, 2, 3, 4]
    remove_duplicates(a, 2)
    print(a)
