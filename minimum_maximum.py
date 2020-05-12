import sys

def minimum_maximum(arr):
    '''Implementing max min/'''
    min_ = sys.maxsize
    max_ = -1 * min_
    for i in arr:
        if min_> i:
            min_ = i
        if max_< i:
            max_ = i
    print(min_, max_)


minimum_maximum([1,-30,7,90,6,-7,89, -4])
