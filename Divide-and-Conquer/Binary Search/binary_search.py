# python3
import math


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    val = my_binary_search(keys, query)
    if val < 0:
        return -1
    return val


def my_binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4
    high, low = len(keys) - 1, 0

    # print(f"h={high} l={low} keys={keys} q={query}")

    # if query > keys[high]:
    #     return high + 1
    # elif query < keys[low]:
    #     return low - 1

    if high < low:
        return -math.inf

    # while high >= low:
    if high >= low:
        mid = (high + low) // 2
        if query == keys[mid]:
            return mid
        if query < keys[mid]:
            # high = mid - 1
            return my_binary_search(keys[:mid], query)
        else:
            return mid + 1 + my_binary_search(keys[mid + 1:], query)
            # low = mid + 1
        # print(f"h={high} m={mid} l={low}")
        # return mid - 1


if __name__ == '__main__':
    input()
    input_keys = list(map(int, input().split()))[:]
    # input_keys = [1, 3, 7, 8, 9, 12, 13]
    # input_queries = [9]
    input()
    input_queries = list(map(int, input().split()))[:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
