from collections import Counter


def parse_input(filename: str):
    segments = []
    with open(filename) as f:
        for line in f:
            x1, y1 = [int(n) for n in line.split(" -> ")[0].split(",")]
            x2, y2 = [int(n) for n in line.split(" -> ")[1].split(",")]
            segments.append(((x1, y1), (x2, y2)))
    return segments


def find_horizontal_vertical_lines(segments):
    return [s for s in segments if s[0][0] == s[1][0] or s[0][1] == s[1][1]]


def get_all_repeated_points(segments):
    points = []
    for segment in segments:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        if x1 == x2:
            points.extend([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
        if y1 == y2:
            points.extend([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])
    counted = Counter(points)
    return set([el for el in counted if counted[el] > 1])


def get_all_repeated_points_for_all_lines(segments):
    points = []
    for segment in segments:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        if x1 == x2:
            points.extend([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
        elif y1 == y2:
            points.extend([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])
        else:
            all_x = [x for x in range(x1, x2 - sign(x1 - x2), -1 * sign(x1 - x2))]
            all_y = [y for y in range(y1, y2 - sign(y1 - y2), -1 * sign(y1 - y2))]
            points.extend([p for p in zip(all_x, all_y)])

    counted = Counter(points)
    return set([el for el in counted if counted[el] > 1])


def sign(a):
    return 1 if a > 0 else -1 if a < 0 else 0


if __name__ == "__main__":
    segments = parse_input('input.txt')
    lines = find_horizontal_vertical_lines(segments)
    repeated_points = get_all_repeated_points(lines)
    print("Solution 1:", len(repeated_points))
    all_repeated_points = get_all_repeated_points_for_all_lines(segments)
    print("Solution 1:", len(all_repeated_points))
