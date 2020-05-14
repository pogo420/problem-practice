import sys


def merge(A, B):
    temp = [0]*(len(A)+len(B))
    # A.append(sys.maxsize)
    # B.append(sys.maxsize)
    i = j = k = 0
    while i < len(A) and j < len(B) and k < len(temp):
        if A[i] < B[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = B[j]
            j += 1
        k += 1

    # adding any missing elements if any
    while i < len(A):
        temp[k] = A[i]
        i+=1
        k+=1

    while j < len(B):
        temp[k] = B[j]
        j+=1
        k+=1

    return temp


if __name__ == "__main__":
    A = [1, 4, 7, 9]
    B = [2, 10, 15,]
    print(A)
    print(B)
    print(merge(A, B))
