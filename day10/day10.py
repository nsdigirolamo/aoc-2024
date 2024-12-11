def read_topography(filename: str) -> list[list[int]]:
    topography = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(int(char))
            topography.append(row)

    return topography

# topography: 2D list of ints (input)
# returns: set of trailheads (value = 0)
def find_trailheads(topography: list[list[int]]) -> set[tuple[int, int]]:
    trailheads = set()
    for row in range(len(topography)):
        for col in range(len(topography[0])):
            if topography[row][col] == 0:
                trailheads.add((row, col))

    return trailheads

# topography: 2D list of ints (input)
# trailhead: starting point of recursive search
# returns: the set of already-visited peaks
def search(topography: list[list[int]], trailhead: tuple[int, int]) -> set[tuple[int, int]]:
    row_count, col_count = len(topography), len(topography[0])
    row, col = trailhead
    current_elevation = topography[row][col]

    peaks = set()

    if current_elevation == 9:
        peaks.add((row, col))

    # top
    if 0 <= row - 1:
        next_elevation = topography[row - 1][col]
        if next_elevation == current_elevation + 1:
            top_peaks = search(topography, (row - 1, col))
            peaks = peaks | top_peaks

    # bottom
    if row + 1 < row_count:
        next_elevation = topography[row + 1][col]
        if next_elevation == current_elevation + 1:
            bottom_peaks = search(topography, (row + 1, col))
            peaks = peaks | bottom_peaks

    # left
    if 0 <= col - 1:
        next_elevation = topography[row][col - 1]
        if next_elevation == current_elevation + 1:
            left_peaks = search(topography, (row, col - 1))
            peaks = peaks | left_peaks

    # right
    if col + 1 < col_count:
        next_elevation = topography[row][col + 1]
        if next_elevation == current_elevation + 1:
            right_peaks = search(topography, (row, col + 1))
            peaks = peaks | right_peaks

    return peaks

# topography: 2D list of ints (input)
# trailhead: starting point of recursive search
# returns: the set of already-visited peaks
def rated_search(topography: list[list[int]], trailhead: tuple[int, int]) -> int:
    row_count, col_count = len(topography), len(topography[0])
    row, col = trailhead
    current_elevation = topography[row][col]

    if current_elevation == 9:
        return 1

    count = 0

    # top
    if 0 <= row - 1:
        next_elevation = topography[row - 1][col]
        if next_elevation == current_elevation + 1:
            count += rated_search(topography, (row - 1, col))

    # bottom
    if row + 1 < row_count:
        next_elevation = topography[row + 1][col]
        if next_elevation == current_elevation + 1:
            count += rated_search(topography, (row + 1, col))

    # left
    if 0 <= col - 1:
        next_elevation = topography[row][col - 1]
        if next_elevation == current_elevation + 1:
            count += rated_search(topography, (row, col - 1))

    # right
    if col + 1 < col_count:
        next_elevation = topography[row][col + 1]
        if next_elevation == current_elevation + 1:
            count += rated_search(topography, (row, col + 1))

    return count

def part_one(topography: list[list[int]]) -> int:
    trailheads = find_trailheads(topography)
    count = 0
    for trailhead in trailheads:
        peaks = search(topography, trailhead)
        count += len(peaks)

    return count

def part_two(topography: list[list[int]]) -> int:
    trailheads = find_trailheads(topography)
    total_rating = 0
    for trailhead in trailheads:
        rating = rated_search(topography, trailhead)
        total_rating += rating

    return total_rating

if __name__ == "__main__":
    topography = read_topography("input.txt")
    result = part_one(topography)
    print(result)
    topography = read_topography("input.txt")
    result = part_two(topography)
    print(result)
