# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    m1 = -1
    m2 = -1
    # must type the -1 condition first
    for i in range(len(numbers)):
        if (m1 == -1) or (numbers[i] > numbers[m1]):
            m1 = i

    for i in range(len(numbers)):
        if ((m2 == -1) or (numbers[i] > numbers[m2])) and (i != m1):
            m2 = i
    # print(f"\n{m1}, {m2}")
    return numbers[m1] * numbers[m2]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
