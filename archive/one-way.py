# one edit cases 
import sys

MAX = 26


def get_freq(s):
    temp = [0]*MAX
    for i in s:
        temp[ord(i)-ord('a')] += 1
    return temp


def distance_check(s1,s2):
    freq1 = get_freq(s1)
    freq2 = get_freq(s2)
#    print(freq1, freq2)
    count = 0
#    print(len(freq1),len(freq2))

    for i in range(MAX):

        if count > 1:
            print("False")
            break
        
        count += abs(freq1[i]-freq2[i])
            
    if count <= 1:
        print("True")


if __name__ == "__main__":
    distance_check(sys.argv[1], sys.argv[2])



