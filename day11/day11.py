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

def blink_optimized(stones: dict[int, int]) -> dict[int, int]:
    new_stones = {}

    for stone, count in stones.items():
        if stone == 0:
            if 1 in new_stones:
                new_stones[1] = new_stones[1] + count
            else:
                new_stones[1] = count
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            halfway = len(str_stone) // 2

            first_half = int(str_stone[:halfway])
            if first_half in new_stones:
                new_stones[first_half] = new_stones[first_half] + count
            else:
                new_stones[first_half] = count

            second_half = int(str_stone[halfway:])
            if second_half in new_stones:
                new_stones[second_half] = new_stones[second_half] + count
            else:
                new_stones[second_half] = count
        else:
            new_stone = stone * 2024
            if new_stone in new_stones:
                new_stones[new_stone] = new_stones[new_stone] + count
            else:
                new_stones[new_stone] = count

    return new_stones

def part_one(stones: list[int]) -> int:
    for _ in range(25):
        stones = blink(stones)

    return len(stones)

def part_two(stones: list[int]) -> int:
    new_stones = {}

    for stone in stones:
        if stone not in new_stones:
            new_stones[stone] = 1
        else:
            new_stones[stone] = new_stones[stone] + 1

    for _ in range(75):
        print(new_stones)
        new_stones = blink_optimized(new_stones)

    print(new_stones)

    total_count = 0
    for stone, count in new_stones.items():
        total_count += count

    return total_count

if __name__ == "__main__":
    stones = read_stones("input.txt")
    result = part_one(stones)
    print(result)
    stones = read_stones("input.txt")
    result = part_two(stones)
    print(result)