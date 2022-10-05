# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(array):
    i = 0
    left, right = 0, len(array) - 1
    return randomized_quick_sort(array, left, right, i)



def partition3(array, left, right,i):
    m1 = left
    m2 = left
    for j in range(left, right):
        if array[j] <= array[right]:
            array[j], array[m1] = array[m1], array[j]
            m1 += 1
        if array[j] == array[right]:
            array[j], array[m2] = array[m2], array[j]
            m2 += 1
    array[m1], array[right] = array[right], array[m1]
    i += 1
    print(i)
    return m1, m2, i


def randomized_quick_sort(array, left, right, i):
    if left >= right:
        return i
    if left < right:
        m1, m2, i = partition3(array, left, right, i)
        i += randomized_quick_sort(array, left, m1 - 1, i)
        i += randomized_quick_sort(array, m2 + 1, right, i)


if __name__ == '__main__':
    # input_n = int(input())
    # elements = list(map(int, input().split()))
    # assert len(elements) == input_n
    elements = [2, 3, 9, 2, 9]
    print(compute_inversions(elements))
