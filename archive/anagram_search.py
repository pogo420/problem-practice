MAX = 256

def compare(x, y):
    for i in range(MAX):
        if x[i] != y[i]:
            return False
    return True


def search(txt, pattern):

    T = len(txt)
    P = len(pattern)

    freq_t = [0]*MAX
    freq_p = [0]*MAX

    # saving for first window
    for i in range(P):
        #print(ord(txt[i]), txt[i])
        freq_t[ord(txt[i])] += 1
        freq_p[ord(pattern[i])] += 1

    for i in range(P, T):
        if compare(freq_t, freq_p):
            print("Boom",i-P)
        #print(i)
        freq_t[ord(txt[i])] += 1 # current character 
        freq_t[ord(txt[i-P])] -= 1 # first character from previous window as its not part of current window


    if compare(freq_t, freq_p):
        print("Boom",T-P)

txt = "BACDGABCDA"
pat = "ABCD"       
search(txt, pat) 
