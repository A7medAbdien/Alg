# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    return fib(n)


def fib(n):
    n = int(n)

    if n <= 1:
        return n

    # we can see that each sequence starts with 01, so gonna track this occurrence
    previousMod, currentMod = 0, 1

    # the sequence of m, for the mod 2 is 011 and for the mod 3 is 01120221
    sequence = [0, 1]
    s = 1

    for i in range(n - 1):
        temp = previousMod
        previousMod = currentMod % 10
        currentMod = (temp + previousMod) % 10
        s = (s + (temp + previousMod) ** 2) % 10
        sequence.append(s)
        if previousMod == 0 and currentMod == 1:
            # now we know the length of the sequence, that was 8 in mod 3 ex.
            index = n % (i + 1)
            # print(f"inside {sequence}")
            return sequence[index]
    # in case the sequence did not finch before the iteration, will get the value in the normal manner and
    # module it
    # print(s)
    return s


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
