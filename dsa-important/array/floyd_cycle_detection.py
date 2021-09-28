# Algorithm:
# p -> 2s
# q -> s
# They will meet if they there is loop.
# Keep one pointer at meeting point
# keep one pointer at the start.
# make the speed same.
# they will meet ast start of loop.
# p -> 2s
# q -> s


# length of loop = l
#                           _
#     m                 /       \
# --------------------(           )
#                       \   _   /


# if they meet at k distance from starting of loop.
# distance by p: m + p * l +k
# distance by q: m + q * l +k
# p will cover more distance
# m + q * l +k = 2(m + p * l +k)
# m+ql+k = 2m+2pl+2k
# m+k = (q-2p) l
# m +k = nl , n is an integer


# reassign p to 0 and q to meeting point. Make speed same.
# p goes m distance q goes m distance.
# and m = nl - k
# so when p goes m distance q goes nl-k -> meets at the staring point of loop


def find_duplicated(data_: list):
    hare = data_[0]
    tortoise = data_[0]

    while True:  # double speed cases
        tortoise = data_[tortoise]
        hare = data_[data_[hare]]
        if hare == tortoise:
            break

    tortoise = data_[0]

    while hare != tortoise:  # simple speed cases
        hare = data_[hare]
        tortoise = data_[tortoise]

    return hare


data_ = [1, 3, 4, 2, 2]


if __name__ == '__main__':
    print(find_duplicated(data_))
