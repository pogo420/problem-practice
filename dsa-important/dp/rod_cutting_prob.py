

def rod_cut(l: list, p: list, max_rod: int, a_l: int) -> int:
    if a_l == 0 or max_rod == 0:
        return 0  # max value or price

    if l[a_l - 1] <= max_rod:
        return max(
            p[a_l - 1] + rod_cut(l, p, max_rod - l[a_l - 1], a_l),
            rod_cut(l, p, max_rod, a_l - 1)
        )
    else:
        return rod_cut(l, p, max_rod, a_l - 1)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    p = [1, 5, 8, 9, 10, 17, 17, 20]

    print(rod_cut(l, p, 8, 8))
