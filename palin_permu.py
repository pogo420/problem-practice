# palindrome in permutation
import sys
MAX = 256

def solve(s):
    freq = [0]*MAX

    for i in s:
        freq[ord(i)] += 1

    odd = 0

    for i in range(MAX):
        if odd > 1:
            print("No")
            break
        
        elif freq[i]&1:
            odd+=1
    if odd <= 1:
        print("Yes")


if __name__ == "__main__":
    solve(sys.argv[1])
