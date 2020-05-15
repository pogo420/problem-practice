from collections import defaultdict


def cal_freq(word):
    freq_list = [0]*26
    for i in word:
        freq_list[ord(i)-ord('a')] += 1
    return "".join(map(str,freq_list))


def group_anagrams(arr):
    anagram_dict = defaultdict(list)
    for i in arr:  # |w| * |n|
        anagram_dict[cal_freq(i)].append(i)

    for i in anagram_dict.keys():
        print(anagram_dict[i])


if __name__ == "__main__":
    arr = ["eat","tea","tan","ate","nat","bat"]
    group_anagrams(arr)
