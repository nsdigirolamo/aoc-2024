def read_garden(filename: str) -> list[list[str]]:
    garden = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            garden.append(row)

    return garden

# Creates an empty garden with the given dimensions.
def get_empty_garden(row_count, col_count) -> list[list[str]]:
    empty_garden = []
    for _ in range(row_count):
        empty_row = []
        for _ in range(col_count):
            empty_row.append('.')
        empty_garden.append(empty_row)

    return empty_garden

# Recursively builds a region, editing the region argument in-place
def build_region(row, col, type: str, garden: list[list[str]], region: list[list[str]]):
    row_count, col_count = len(garden), len(garden[0])
    if (
        row < 0 or
        col < 0 or
        row_count <= row or
        col_count <= col or
        garden[row][col] != type or
        region[row][col] == type
    ):
        return

    region[row][col] = type

    build_region(row - 1, col, type, garden, region)
    build_region(row + 1, col, type, garden, region)
    build_region(row, col - 1, type, garden, region)
    build_region(row, col + 1, type, garden, region)

# Returns a garden where only a single region is visible. This region
# will be region that the plot at (row, col) belongs to.
def get_region(row, col, garden: list[list[str]]) -> list[list[str]]:
    row_count, col_count = len(garden), len(garden[0])
    region = get_empty_garden(row_count, col_count)
    build_region(row, col, garden[row][col], garden, region)
    return region

def calculate_region_area(region: list[list[str]]):
    area = 0
    for row in region:
        for plot in row:
            if plot != '.':
                area += 1

    return area

def calculate_region_perimeter(region: list[list[str]]):
    row_count, col_count = len(region), len(region[0])
    total_perimeter = 0
    for row in range(row_count):
        for col in range(col_count):
            if region[row][col] != '.':
                perimeter = 0

                # If a plot is at the edge of the garden, we need to count that.
                if row == 0:
                    perimeter += 1
                if row + 1 == row_count:
                    perimeter += 1
                if col == 0:
                    perimeter += 1
                if col + 1 == row_count:
                    perimeter += 1

                if 0 <= row - 1 and region[row - 1][col] == '.':
                    perimeter += 1
                if row + 1 < row_count and region[row + 1][col] == '.':
                    perimeter += 1
                if 0 <= col - 1 and region[row][col - 1] == '.':
                    perimeter += 1
                if col + 1 < col_count and region[row][col + 1] == '.':
                    perimeter += 1

                total_perimeter += perimeter

    return total_perimeter

def part_one(garden: list[list[str]]) -> int:
    row_count, col_count = len(garden), len(garden[0])
    tracker_garden = get_empty_garden(row_count, col_count)
    total_price = 0

    for row in range(row_count):
        for col in range(col_count):
            # print(row, col)
            # for i in tracker_garden:
            #    print(i)
            # print()
            # only look for a region here if the tracker is empty
            if (tracker_garden[row][col] == '.'):
                # Get the region at this location and calc the price
                region = get_region(row, col, garden)

                # for i in region:
                #     print(i)

                area = calculate_region_area(region)
                perimeter = calculate_region_perimeter(region)
                price = area * perimeter
                total_price += price
                # print("area:", area)
                # print("perimeter:", perimeter)
                # print("price:", price)

                # Fill this region into our tracker garden so we know we've visited
                for i in range(row_count):
                    for j in range(col_count):
                        if (region[i][j] != '.'):
                            tracker_garden[i][j] = region[i][j]
            # print("total_price", total_price)

    return total_price

if __name__ == "__main__":
    garden = read_garden("input.txt")
    result = part_one(garden)
    print(result)