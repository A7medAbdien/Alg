# python3

from random import randint


def partition3(array, left, right):
    m1= left
    m2= left
    # print(f"------------- {left} {right} {m1} {m2} {array}")
    for j in range(left, right):
        # print(f"--- {left} {right} {m1} {m2} {array}")
        # print(f"out j: {array[j]} right: {array[right]} m: {array[m]}")
        if array[j] <= array[right]:
            # print(f"j: {array[j]} right: {array[right]} m: {array[m]}")
            array[j], array[m1] = array[m1], array[j]
            m1 += 1
            # m2 += 1
            # print(f"less: ", m1, m2)
        if array[j] == array[right]:
            array[j], array[m2] = array[m2], array[j]
            m2 += 1
            # print("eq:", m1, m2)

    array[m1], array[right] = array[right], array[m1]
    # print(m, right, array)
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    # k = randint(left, right)
    # array[left], array[k] = array[k], array[left]
    if left < right:
        m1, m2 = partition3(array, left, right)
        # print(m1)
        randomized_quick_sort(array, left, m1-1)
        randomized_quick_sort(array, m2 + 1, right)
        # print(array)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    # elements = [3,2,1]
    # elements = [2, 3, 9, 2, 9]
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
