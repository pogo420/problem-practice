# aabbc -->a2b2c1
import sys
MAX = 26

def get_freq(s):
    temp = [0] * MAX
    for i in s:
        temp[ord(i)-ord('a')] += 1
    return temp

def string_compress(s):
    freq = get_freq(s)
    temp = "".join([chr(inx+ord('a')) + str(i)  for inx, i in enumerate(freq) if i!=0])

   # similar to ternary  
    print(temp) if len(s)>len(temp) else print(s)


string_compress(sys.argv[1])

