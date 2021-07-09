import sys

def partition(arr, low, high):
    # [1,6,8,9] low = 0 high = 3
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if pivot >= arr[j]:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        print(arr)

    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    print(arr)
    print(i+1)


if __name__ == "__main__":
    partition(list(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))




