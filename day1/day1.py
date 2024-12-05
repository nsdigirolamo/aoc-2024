def read_pairs(filename: str) -> tuple[list[int], list[int]]:
    left = []
    right = []

    with open(filename, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.strip().split())
            left.append(num1)
            right.append(num2)

    return left, right

def main(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    distance = 0

    for l, r in zip(left, right):
        distance += abs(l - r)

    return distance

if __name__=="__main__":
    lists = read_pairs("./input.txt")
    distance = main(lists[0], lists[1])
    print(distance)