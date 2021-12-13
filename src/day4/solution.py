def parse_input(filename: str):
    with open(filename) as f:
        numbers = [int(l) for l in f.readline().split(",")]
        content = f.read().split("\n")
    content = content[1:]
    grids = [[[int(i) for i in l.split(" ") if i != ""] for l in content[n:n + 5]] for n in range(0, len(content), 6)]
    return numbers, grids


def is_winner(updated_grid: list):
    if ["X", "X", "X", "X", "X"] in updated_grid:
        return True
    columns = [[l[i] for l in updated_grid] for i in range(5)]
    if ["X", "X", "X", "X", "X"] in columns:
        return True
    return False


def find_winner_grid(grids: list, numbers: list[int]):
    grids_copy = grids.copy()
    for number in numbers:
        for c in range(len(grids)):
            updated_grid = [[i if type(i) == int and i != number else "X" for i in line] for line in grids_copy[c]]
            if is_winner(updated_grid):
                return updated_grid, number
            grids_copy[c] = updated_grid


def find_loser_grid(grids: list, numbers: list[int]):
    grids_copy = grids.copy()
    indexes = set(range(len(grids_copy)))
    winners = []
    for n in numbers:
        indexes_to_drop = set([])
        for c in indexes:
            updated_grid = [[i if type(i) == int and i != n else "X" for i in line] for line in grids_copy[c]]
            if is_winner(updated_grid):
                indexes_to_drop.add(c)
                winners.append((updated_grid, n))
            else:
                grids_copy[c] = updated_grid
        indexes = indexes.difference(indexes_to_drop)
    return winners.pop()


def sum_unmarked_numbers(grid):
    return sum([sum([number for number in l if type(number) == int]) for l in grid])


if __name__ == "__main__":
    numbers, grids = parse_input('input.txt')
    winner, number = find_winner_grid(grids, numbers)
    print("Solution 1:", sum_unmarked_numbers(winner) * number)
    loser, n = find_loser_grid(grids, numbers)
    print("Solution 2:", sum_unmarked_numbers(loser) * n)
