def read_map(filename: str) -> list[list[int]]:
    guard_map = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            guard_map.append(row)

    return guard_map

def find_guard(map: list[list[int]]) -> tuple[int, int]:
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                return i, j

    return 0, 0

def walk_map(map: list[list[int]]) -> list[list[int]]:
    guard_row, guard_col = find_guard(map)
    row_count, col_count = len(map), len(map[0])
    guard_facing = "up"

    map[guard_row][guard_col] = 'X' # Place an X at the starting position.

    while (
        not (
            (guard_facing == "up" and guard_row == 0) or
            (guard_facing == "down" and guard_row == row_count - 1) or
            (guard_facing == "left" and guard_col == 0) or
            (guard_facing == "right" and guard_col == col_count - 1)
        )
    ):
        if guard_facing == "up":
            if map[guard_row - 1][guard_col] != '#':
                guard_row -= 1
            else:
                guard_facing = "right"

        if guard_facing == "right":
            if map[guard_row][guard_col + 1] != '#':
                guard_col += 1
            else:
                guard_facing = "down"

        if guard_facing == "down":
            if map[guard_row + 1][guard_col] != '#':
                guard_row += 1
            else:
                guard_facing = "left"

        if guard_facing == "left":
            if map[guard_row][guard_col - 1] != '#':
                guard_col -= 1
            else:
                guard_facing = "up"

        map[guard_row][guard_col] = 'X'

    return map

def count_x(map: list[list[int]]):
    count = 0
    for row in map:
        for char in row:
            if char == 'X':
                count += 1

    return count

def part_one(map: list[list[int]]) -> int:
    walked_map = walk_map(map)
    return count_x(walked_map)

if __name__ == "__main__":
    guard_map = read_map("input.txt")
    result = part_one(guard_map)
    print(result)
