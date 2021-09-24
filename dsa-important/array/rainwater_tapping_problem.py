
def max_water(data: list) -> int:
    left = [0]*len(data)
    right = [0]*len(data)

    i = 0
    while i < len(data):
        left[i] = max(data[0:i+1])  # max in left
        right[i] = max(data[i:])  # max in right
        i += 1

    i = 0
    rain_water = 0
    while i < len(data):
        rain_water += (min(left[i], right[i]) - data[i])  # for each index get min of both ends - height of building
        i += 1

    return rain_water


if __name__ == '__main__':
    d = [3, 1, 2, 4, 0, 1, 3, 2]
    print(max_water(d))
