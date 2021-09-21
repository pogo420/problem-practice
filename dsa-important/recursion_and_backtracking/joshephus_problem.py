# holder will kill kth person including the holder. Transfer the gun to the person, next to deceased.
# check notes

def joshef(n, k):
    if n == 1:  # base case
        return 0  # zero is the index of single element
    return (joshef(n-1, k) + k) % n
