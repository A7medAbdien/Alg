# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    # we can see that each sequence starts with 01, so gonna track this occurrence
    previousMod, currentMod = 0, 1

    # the sequence of m, for the mod 2 is 011 and for the mod 3 is 01120221
    sequence = [0, 1]

    for i in range(n - 1):
        temp = previousMod
        previousMod = currentMod % m
        currentMod = (temp + previousMod) % m
        sequence.append(currentMod)
        if previousMod == 0 and currentMod == 1:
            # now we know the length of the sequence, that was 8 in mod 3 ex.
            index = n % (i + 1)
            return sequence[index]
    # in case the sequence did not finch before the iteration, will get the value in the normal manner and
    # module it
    return currentMod


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
