def read_map(filename: str) -> list[list[str]]:
    guard_map = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            guard_map.append(row)

    return guard_map

def find_guard(map: list[list[str]]) -> tuple[int, int]:
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                return i, j
    return 0, 0

def walk_map(map: list[list[str]]) -> list[list[str]]:
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

def check_for_loop(map) -> bool:
    row, col = find_guard(map)
    row_count, col_count = len(map), len(map[0])
    facing = "up"

    max_steps = row_count * col_count
    steps = 0

    while (
        not (
            (facing == "up"    and row == 0            ) or
            (facing == "down"  and row == row_count - 1) or
            (facing == "left"  and col == 0            ) or
            (facing == "right" and col == col_count - 1)
        )
    ):
        next_row, next_col = row, col
        if facing == "up":
            next_row = row - 1
        elif facing == "down":
            next_row = row + 1
        elif facing == "left":
            next_col = col - 1
        elif facing == "right":
            next_col = col + 1

        next_cell = map[next_row][next_col]

        if next_cell == '#':
            if facing == "up":
                facing = "right"
            elif facing == "down":
                facing = "left"
            elif facing == "left":
                facing = "up"
            elif facing == "right":
                facing = "down"
        else:
            row = next_row
            col = next_col

        steps += 1
        if max_steps < steps:
            return True

    return False

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

def part_two(map: list[list[str]]) -> int:
    count = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            print(f"Checking {row}, {col}, {count}")
            if map[row][col] != '^' and map[row][col] != '#':
                map[row][col] = '#'
                is_loop = check_for_loop(map)
                if is_loop:
                    print(is_loop)
                    count += 1
                map[row][col] = '.'

    return count

if __name__ == "__main__":
    guard_map = read_map("input.txt")
    result = part_one(guard_map)
    print(result)
    guard_map = read_map("input.txt")
    result = part_two(guard_map)
    print(result)
