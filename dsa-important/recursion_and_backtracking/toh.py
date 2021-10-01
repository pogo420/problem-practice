pillars = ["A", "B", "C"]


def toh(n, source, destination, helper):
    if n == 1:
        print(f"move disk {n} from {source} to {destination}")
        return
    toh(n - 1, source, helper, destination)
    print(f"move disk {n} from {source} to {destination}")
    toh(n - 1, helper, destination, source)


if __name__ == '__main__':
    toh(3, "A", "C", "B")
