def read_pairs(filename: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    with open(filename, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.strip().split())
            left.append(num1)
            right.append(num2)
    return left, right

def part1(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    distance = 0
    for l, r in zip(left, right):
        distance += abs(l - r)
    return distance

def part2(left: list[int], right: list[int]) -> int:
    similarity = 0
    for l in left:
        for r in right:
            if l == r:
                similarity += l
    return similarity

if __name__=="__main__":
    left, right = read_pairs("./input.txt")
    distance = part1(left, right)
    print(distance)
    similarity = part2(left, right)
    print(similarity)