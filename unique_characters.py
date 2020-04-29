# space complexity: 1 ,time complexity: n
import sys
MAX = 256

def main(string):
    lookup = [0]*MAX
    count = 0
    for i in string:
        if lookup[ord(i)] == 0:
            lookup[ord(i)] = 1
            count += 1
        else:
            print("No")
            break

    if count == len(string):
        print("Yes")


if __name__ == "__main__":
    main(sys.argv[1])




