def read_word_search(filename: str) -> list[list[str]]:
    word_search = []
    with open(filename, 'r') as file:
        for line in file:
            chars = []
            for char in line:
                chars.append(char)
            word_search.append(chars)
    return word_search

def check_for_xmas(word_search: list[list[str]], row: int, col: int) -> int:
    count = 0
    row_count = len(word_search)
    col_count = len(word_search[0])
    # Left to right
    if word_search[row][col:col+4] == ['X', 'M', 'A', 'S']:

        count += 1
    # Right to left.
    if word_search[row][col-4:col] == ['S', 'A', 'M', 'X']:
        count += 1
    # Top to bottom.
    if (
        (row + 3 < row_count) and
        word_search[row][col]     == 'X' and
        word_search[row + 1][col] == 'M' and
        word_search[row + 2][col] == 'A' and
        word_search[row + 3][col] == 'S'
    ):
        count += 1
    # Bottom to top.
    if (
        not (row - 3 < 0) and
        word_search[row - 3][col] == 'S' and
        word_search[row - 2][col] == 'A' and
        word_search[row - 1][col] == 'M' and
        word_search[row][col]     == 'X'
    ):
        count += 1
    # Top left to bottom right.
    if (
        (row + 3 < row_count) and (col + 3 < col_count) and
        word_search[row][col]         == 'X' and
        word_search[row + 1][col + 1] ==  'M' and
        word_search[row + 2][col + 2] ==   'A' and
        word_search[row + 3][col + 3] ==    'S'
    ):
        count += 1
    # Bottom right to top left.
    if (
        not (row - 3 < 0) and not (col - 3 < 0) and
        word_search[row - 3][col - 3] == 'S' and
        word_search[row - 2][col - 2] ==  'A' and
        word_search[row - 1][col - 1] ==   'M' and
        word_search[row][col]         ==    'X'
    ):
        count += 1
    # Top right to bottom left.
    if (
        (row + 3 < row_count) and not (col - 3 < 0) and
        word_search[row][col]         ==    'X' and
        word_search[row + 1][col - 1] ==   'M' and
        word_search[row + 2][col - 2] ==  'A' and
        word_search[row + 3][col - 3] == 'S'
    ):
        count += 1
    # Bottom left to top right.
    if (
        not (row - 3 < 0) and (col + 3 < col_count) and
        word_search[row - 3][col + 3] ==    'S' and
        word_search[row - 2][col + 2] ==   'A' and
        word_search[row - 1][col + 1] ==  'M' and
        word_search[row][col]         == 'X'
    ):
        count += 1

    return count

def part_one(word_search: list[list[str]]) -> int:
    count = 0
    for row in range(len(word_search)):
        for col in range(len(word_search[0])):
            count += check_for_xmas(word_search, row, col)

    return count

if __name__=="__main__":
    word_search = read_word_search("input.txt")
    result = part_one(word_search)
    print(result)
