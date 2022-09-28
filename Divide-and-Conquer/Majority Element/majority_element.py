# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        # print(f"{e} {elements.count(e)} {len(elements) // 2}")
        if (elements.count(e) > len(elements) // 2) & (len(elements) // 2 != 0):
            return 1
            break
        return 0 + majority_element(elements[len(elements) // 2:0]) + majority_element(elements[:len(elements) // 2])
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    # input_elements = [1, 2, 3, 4]
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
    # print(majority_element_naive(input_elements))
