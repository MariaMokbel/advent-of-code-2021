from typing import List


def parse_input(filename: str) -> List:
    directions = []
    with open(filename) as f:
        for line in f:
            directions.append((line.split()[0], int(line.split()[1])))

    return directions


def get_position(directions):
    aim = 0
    depth = 0
    forward = 0
    for direction in directions:
        if direction[0] == "forward":
            depth += aim * direction[1]
            forward += direction[1]
        elif direction[0] == "up":
            aim -= direction[1]
        else:
            aim += direction[1]
    return depth, forward


if __name__ == "__main__":
    directions = parse_input('input.txt')
    horizontal, depth = get_position(directions)
    print("Solution 2:", horizontal*depth)
