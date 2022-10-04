# python3

from random import randint


def partition3(array, left, right):
    m1= left
    m2= left
    # print(f"------------- {left} {right} {m} {array}")
    for j in range(left, right):
        # print(f"out j: {array[j]} right: {array[right]} m: {array[m]}")
        if array[j] < array[right]:
            # print(f"j: {array[j]} right: {array[right]} m: {array[m]}")
            array[j], array[m1] = array[m1], array[j]
            m1 += 1
            m2 += 1
            # print(m)
        if array[j] == array[right]:
            array[j], array[m2] = array[m2], array[j]
            m2 += 1
    array[m2], array[right] = array[right], array[m2]
    # print(m, right, array)
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    # k = randint(left, right)
    # array[left], array[k] = array[k], array[left]
    if left < right:
        m1,m2 = partition3(array, left, right)
        # print(m1)
        randomized_quick_sort(array, left, m1-1)
        randomized_quick_sort(array, m2 + 1, right)
        # print(array)


if __name__ == '__main__':
    # input_n = int(input())
    # elements = list(map(int, input().split()))
    elements = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    # assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
