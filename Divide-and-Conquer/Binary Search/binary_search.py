# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    high, low = len(keys)-1, 0

    # print(f"h={high} l={low} keys={keys} q={query}")

    # if query > keys[high]:
    #     return high + 1
    # elif query < keys[low]:
    #     return low - 1

    while high >= low:
        mid = (high + low) // 2
        if query == keys[mid]:
            return mid
        elif query < keys[mid]:
            high = mid - 1
        else:
            low = mid + 1
        # print(f"h={high} m={mid} l={low}")
    else:
        return -1
        # return mid - 1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    # input_keys = [2575, 10995, 11718, 12619, 13116, 21303, 23065, 25750, 28039, 28135, 28495, 32691, 38164, 48456, 49914, 51890, 52946, 54565, 56544, 62162, 64574, 65893, 66551, 67928, 69416, 69932, 76225, 76350, 79936, 85140, 90302, 90831, 100657, 100922, 102026, 102901, 110057, 111382, 114642, 115265, 117882, 120202, 120886, 125069, 125863, 126030, 127810, 131034, 131563, 133152, 138882, 140738, 142503, 144881, 145574, 148655, 150178, 150186, 151580, 153798, 153885, 154332, 155761, 159554, 160739, 162218, 165455, 165880, 166369, 167514, 173866, 174049, 174167, 178038, 179104, 180401, 185185, 188517, 192657, 197941, 198477, 200171, 205307, 205698, 207820, 214376, 217442, 222329, 223046, 224310, 225564, 225715, 226490, 228928, 229133, 231799, 233731, 234556, 235042, 237078]
    # input_queries = [125864]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
        print(linear_search(input_keys, q))
