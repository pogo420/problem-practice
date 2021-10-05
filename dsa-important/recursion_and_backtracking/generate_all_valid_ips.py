

def is_valid_ip(s: str):

    if s.startswith("0") and len(s) > 1:
        return False
    elif s == "":
        return False
    elif 0 <= int(s) <= 255:
        return True
    else:
        return False


def generate_ip(s, start, width, result: list, current_pattern: list):

    if len(current_pattern) == 4:
        result.append(current_pattern.copy())
        return

    if is_valid_ip(s[start: start + width]):
        current_pattern.append(s[start: start + width])
        generate_ip(s, start + width, width, result, current_pattern)

    elif width > 0 and len(current_pattern) > 0:
        current_pattern.pop()
        generate_ip(s, start, width-1, result, current_pattern)


def generate_ip_v2(s, start, width, result: list, current_pattern: list):
    print(start, width, result, current_pattern)

    if len(current_pattern) == 4:
        result.append(current_pattern.copy())
        return

    if is_valid_ip(s[start: start + width]):
        current_pattern.append(s[start: start + width])
        generate_ip(s, start + width, width + 1, result, current_pattern)

    current_pattern.pop()
    generate_ip(s, start, width, result, current_pattern)


if __name__ == '__main__':
    s = "25525511135"
    c = []
    r = []
    # generate_ip(s, 0, 3, r, c)
    generate_ip_v2(s, 0, 1, r, c)
    print(r)
