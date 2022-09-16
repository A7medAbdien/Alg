# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    f1 = fib(max(to_index, from_index))
    f2 = fib(min(to_index, from_index)-1)
    # print(f"{int(f1)}  {int(f2)}")
    return (f1 - f2) % 10


def fib(n):
    n = int(n)

    if n < 0:
        return 0

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
        s = (s + temp + previousMod) % 10
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
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
