from typing import Dict, List


def parse_input(filename: str) -> Dict[str, list[int]]:
    directions = {}
    with open(filename) as f:
        for line in f:
            try:
                directions[line.split()[0]].append(int(line.split()[1]))
            except KeyError:
                directions[line.split()[0]] = [(int(line.split()[1]))]

    return directions


def get_horizontal_position(directions):
    return sum(directions["forward"])


def get_depth(directions):
    return sum(directions["down"]) - sum(directions["up"])


if __name__ == "__main__":
    directions = parse_input('input.txt')
    horizontal = get_horizontal_position(directions)
    depth = get_depth(directions)
    print("Solution 1:", depth * horizontal)
    # print("Solution 2:", get_increased_measurement_sum(measurements))
