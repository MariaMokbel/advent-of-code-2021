from typing import List, Tuple


def parse_input(filename: str) -> List:
    with open(filename) as f:
        content = f.read()

    return content.split("\n")


def get_rate(diagnostic_report: List[str]) -> Tuple[int, int]:
    compt = [0] * len(diagnostic_report[0])
    for number in diagnostic_report:
        for i in range(len(number)):
            compt[i] += int(number[i])

    gamma_rate = list(map(lambda x: "1" if x > len(diagnostic_report) // 2 else "0", compt))
    epsilon_rate = list(map(lambda x: "0" if x > len(diagnostic_report) // 2 else "1", compt))
    return int("".join(gamma_rate), 2), int("".join(epsilon_rate), 2)


def get_ratings(diagnostic_report: List[str]):
    oxygen_rating = diagnostic_report
    co2_rating = diagnostic_report

    for i in range(len(diagnostic_report[0])):
        list_with_1 = []
        list_with_0 = []
        if len(oxygen_rating) != 1:
            for number in oxygen_rating:
                if number[i] == "1":
                    list_with_1.append(number)
                else:
                    list_with_0.append(number)
            if len(list_with_1) >= len(list_with_0):
                oxygen_rating = list_with_1
            else:
                oxygen_rating = list_with_0

        list_with_1 = []
        list_with_0 = []
        if len(co2_rating) != 1:
            for n in co2_rating:
                if n[i] == "1":
                    list_with_1.append(n)
                else:
                    list_with_0.append(n)
            if len(list_with_1) >= len(list_with_0):
                co2_rating = list_with_0
            else:
                co2_rating = list_with_1

    return int(oxygen_rating[0], 2), int(co2_rating[0], 2)


if __name__ == "__main__":
    diagnostic = parse_input("input.txt")
    gamma, epsilon = get_rate(diagnostic)
    oxygen_rating, co2_rating = get_ratings(diagnostic)
    print("Solution 1", gamma * epsilon)
    print("Solution 2", oxygen_rating * co2_rating)
