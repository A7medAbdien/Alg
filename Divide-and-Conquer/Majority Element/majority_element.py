# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    # print(elements)

    m = len(elements)//2
    a = most(elements[m:])
    b = most(elements[:m])
    # print(f"a: {a}")
    # print(f"b: {b}")
    if list == type(a):
        if b in a:
            if elements.count(b)> len(elements)//2:
                return 1
    if list == type(b):
        if a in b:
            if elements.count(a) > len(elements) // 2:
                return 1
    if (list != type(a)) or (list != type(b)):
        if a == b:
            if elements.count(a) > len(elements) // 2:
                return 1
    return 0


def most(elements):
    # print(elements)
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return e
    return elements


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    # input_elements = [8, 1, 5, 111, 5, 11, 5, 5, 5, 11111]
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
    # print(majority_element_naive(input_elements))
