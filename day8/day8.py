def read_locations(filename: str) -> list[list[str]]:
    locations = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            locations.append(row)

    return locations

def map_frequencies(location: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    row_count, col_count = len(locations), len(locations[0])

    # Dictionary that maps frequencies to a list of antenna locations.
    frequencies: dict[str, list[tuple[int, int]]] = {}
    for row in range(row_count):
        for col in range(col_count):
            location = locations[row][col]
            # If the location has an antenna, add it to the frequency dict.
            if location != '.':
                if location not in frequencies:
                    frequencies[location] = []
                frequencies[location].append((row, col))

    return frequencies

def mark_antinodes(locations: list[list[str]]) -> list[list[str]]:
    row_count, col_count = len(locations), len(locations[0])
    frequencies = map_frequencies(locations)

    # Antinodes list will store all unique locations of antinodes.
    antinodes = [ ['.'] * col_count for _ in range(row_count) ]
    for _, locations in frequencies.items():
        # For every location pair, we check if the antinode is in bounds.
        for index, current_location in enumerate(locations):
            other_locations = locations[:index] + locations[index + 1:]
            for other_location in other_locations:
                # First get the offset between the two locations
                row_offset = current_location[0] - other_location[0]
                col_offset = current_location[1] - other_location[1]
                # Then add to current location to find possible antinode
                antinode_row = current_location[0] + row_offset
                antinode_col = current_location[1] + col_offset
                # If the antinode isn't out of bounds, add it to the list.
                if (
                    (0 <= antinode_row and antinode_row < row_count) and
                    (0 <= antinode_col and antinode_col < col_count)
                ):
                    antinodes[antinode_row][antinode_col] = '#'

    return antinodes

def mark_antinodes_with_harmonics(locations: list[list[str]]) -> list[list[str]]:
    row_count, col_count = len(locations), len(locations[0])
    frequencies = map_frequencies(locations)

    # Antinodes list will store all unique locations of antinodes.
    antinodes = [ ['.'] * col_count for _ in range(row_count) ]
    for _, locations in frequencies.items():
        # For every location pair, we check if the antinode is in bounds.
        for index, current_location in enumerate(locations):
            other_locations = locations[:index] + locations[index + 1:]
            for other_location in other_locations:
                # First get the offset between the two locations
                row_offset = current_location[0] - other_location[0]
                col_offset = current_location[1] - other_location[1]
                # Now just keep adding until the antinode is out of bounds.
                antinode_row = current_location[0]
                antinode_col = current_location[1]
                multiplier = 0
                while (
                    (0 <= antinode_row and antinode_row < row_count) and
                    (0 <= antinode_col and antinode_col < col_count)
                ):
                    antinodes[antinode_row][antinode_col] = '#'
                    multiplier += 1
                    antinode_row = current_location[0] + row_offset * multiplier
                    antinode_col = current_location[1] + col_offset * multiplier

    return antinodes

def count_antinodes(antinodes: list[list[str]]) -> int:
    count = 0
    for row in antinodes:
        for location in row:
            if location == '#':
                count += 1

    return count

def part_one(locations: list[list[str]]) -> int:
    antinodes = mark_antinodes(locations)
    count = count_antinodes(antinodes)

    return count

def part_two(locations: list[list[str]]) -> int:
    antinodes = mark_antinodes_with_harmonics(locations)
    count = count_antinodes(antinodes)

    return count

if __name__ == "__main__":
    locations = read_locations("input.txt")
    result = part_one(locations)
    print(result)
    locations = read_locations("input.txt")
    result = part_two(locations)
    print(result)
