from typing import List


def parse_input(filename: str) -> List[int]:
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def get_increased_measurement_number(measurements: List[int]) -> int:
    return len([measurements[i + 1] for i in range(len(measurements) - 1) if measurements[i + 1] > measurements[i]])


def get_increased_measurement_sum(measurements: List[int]) -> int:
    sums = [measurements[i] + measurements[i + 1] + measurements[i + 2] for i in range(len(measurements) - 2)]
    return get_increased_measurement_number(sums)


if __name__ == "__main__":
    measurements = parse_input('input.txt')
    print("Solution 1:", get_increased_measurement_number(measurements))
    print("Solution 2:", get_increased_measurement_sum(measurements))
