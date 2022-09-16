# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     a, b = 0, 1
    #     for i in range(2, n + 1):
    #         c = (a + b) % 10
    #         a = b
    #         b = c
    #
    #     return c
    if n <= 1:
        return n

    # we can see that each sequence starts with 01, so gonna track this occurrence
    previousMod, currentMod = 0, 1

    # the sequence of m, for the mod 2 is 011 and for the mod 3 is 01120221
    sequence = [0, 1]

    for i in range(n - 1):
        temp = previousMod
        previousMod = currentMod % 10
        currentMod = (temp + previousMod) % 10
        sequence.append(currentMod)
        if previousMod == 0 and currentMod == 1:
            # now we know the length of the sequence, that was 8 in mod 3 ex.
            index = n % (i + 1)
            return sequence[index]
    # in case the sequence did not finch before the iteration, will get the value in the normal manner and
    # module it
    return currentMod


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
