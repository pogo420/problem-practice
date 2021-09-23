# discuss O(n^2)
# discuss O(n) solutions

def max_profit_1(data: list) -> int:

    # calculating auxiliary data, max from that point till end.
    # we get max value in future from that point we can easy calculate the diff
    # O(n) time and space
    aux: list = [0] * len(data)
    i = len(data) - 1
    while i >= 0:
        aux[i] = max(data[i:])
        i -= 1

    j = 0
    max_diff = 0
    while j < len(data):
        max_diff = max(max_diff, aux[j] - data[j])
        j += 1

    return max_diff


def max_profit_2(data: list) -> int:
    # we get min value in past from that point we can easy calculate the diff
    # O(n) time O(1) space
    local_min = data[0]
    max_diff = 0

    for d in data:
        local_min = min(local_min, d)
        max_diff = max(max_diff, d - local_min)

    return max_diff


def max_profit_multiple_sell(data: list):
    profit = 0
    i = 1
    while i < len(data):
        if data[i] > data[i-1]:  # buy during local min , sell during local max
            profit += (data[i] - data[i-1])
        i += 1
    return profit


if __name__ == '__main__':
    a = [3, 1, 4, 8, 7, 2, 5]
    print(max_profit_1(a))
    print(max_profit_2(a))

    s = [5, 2, 7, 3, 6, 1, 2, 4]
    print(max_profit_multiple_sell(s))

