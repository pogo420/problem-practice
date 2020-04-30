from collections import defaultdict

MAX = 26


def get_anagram_string(w):
    '''Function to convert a freq array into string'''
    temp = [0]*MAX
    for i in w:
        temp[ord(i)-ord('a')] += 1
    return "".join(map(str, temp))


def anagram_grouping(s):
    ''' Using deafult dict for analysis '''
    master = defaultdict(list)
    for i in s:
       master[get_anagram_string(i)].append(i)

    for i in master.keys():
        print(master[i])


if __name__ =="__main__":
    arr = ["eat","tea","tan","ate","nat","bat"]
    anagram_grouping(arr)
