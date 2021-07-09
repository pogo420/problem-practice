import sys
MAX = 256

def main(s1, s2):
    freqa = [0]*MAX
    freqb = [0]*MAX
    if len(s1) != len(s2):
        return "No"

    for i in range(len(s1)):
        freqa[ord(s1[i])] += 1
        freqb[ord(s2[i])] += 1

    for i in range(MAX):
        if freqa[i] != freqb[i]:
            return "No"
    return "Yes"


if __name__ == "__main__":
    print(main(sys.argv[1],sys.argv[2]))


    

