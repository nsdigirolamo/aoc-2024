def read_stones(filename: str) -> list[int]:
    stones = []
    with open(filename, 'r') as file:
        for line in file:
            for char in line.strip().split():
                stones.append(int(char))

    return stones

def blink(stones: list[int]) -> list[int]:
    i = 0

    while (i < len(stones)):
        stone = stones[i]

        if stone == 0:
            stones[i] = 1
            i += 1
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            halfway = len(str_stone) // 2
            stones[i] = int(str_stone[:halfway])
            stones.insert(i + 1, int(str_stone[halfway:]))
            i += 2
        else:
            stones[i] = stone * 2024
            i += 1

    return stones


def part_one(stones: list[int]) -> int:
    for _ in range(25):
        stones = blink(stones)

    return len(stones)

if __name__ == "__main__":
    stones = read_stones("input.txt")
    result = part_one(stones)
    print(result)