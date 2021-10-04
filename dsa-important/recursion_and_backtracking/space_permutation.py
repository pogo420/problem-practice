# abc = abc, a_bc, ab_c, a_b_c

def permu_space(s, result: list, curr_str, pos):
    if pos == len(s) - 1:
        result.append(curr_str+s[-1])
        return

    permu_space(s, result, curr_str + s[pos] + "_", pos + 1)
    permu_space(s, result, curr_str + s[pos], pos + 1)


if __name__ == '__main__':
    s = "abcd"
    r = []
    permu_space(s, r, "", 0)
    print(r)
