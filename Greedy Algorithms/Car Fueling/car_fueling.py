# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    location, result = 0, 0

    while stops:
        if location + m >= d:
            return result
        if (location + m < d) and (location + m < stops[0]):
            return -1
        new_location = location
        while stops and (location + m < d) and (location + m >= stops[0]):
            # print(f" stops={stops} Cloc={new_location} loc={location} result={result}")
            new_location = stops[0]
            stops.pop(0)
        result += 1
        # print(f"out result={result}")
        location = new_location
    if location + m < d:
        return -1
    return result


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
