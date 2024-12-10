def read_disk(filename: str) -> list[str]:
    disk = []
    with open(filename, 'r') as file:
        for line in file:
            for index, char in enumerate(line.strip()):
                for _ in range(int(char)):
                    if index % 2 == 0:
                        disk.append(str(index // 2))
                    else:
                        disk.append('.')

    return disk

def read_disk_without_expansion(filename: str) -> list[str]:
    disk = []
    with open(filename, 'r') as file:
        for line in file:
            for char in line.strip():
                disk.append(char)

    return disk

def calculate_checksum(disk: list[str]):
    checksum = 0
    for index, char in enumerate(disk):
        if char != '.':
            checksum += index * int(char)

    return checksum

def calculate_disk_size(disk: list[str]) -> int:
    size = 0
    for char in disk:
        if char != '.':
            size += int(char)

    return size

def compact_disk(disk: list[str]) -> list[str]:
    left = 0
    right = len(disk) - 1
    while (left < right):
        while (disk[left] != '.'):
            left += 1
        while (disk[right] == '.'):
            right -= 1
        disk[left] = disk[right]
        disk[right] = '.'

    # The right and left pointers above can "pass" each other and swap the final
    # two blocks improperly. This if statement swaps them back.
    if disk[right] == '.' and disk[left] != '.':
        disk[right] = disk[left]
        disk[left] = '.'

    return disk

def compact_disk_without_fragmentation(disk: list[str]) -> list[str]:

    right = len(disk) - 1
    while (0 <= right):
        # If the right pointer is '.', then move right and look for a file ID.
        if disk[right] == '.':
            right -= 1
        else:
            id = disk[right]
            # Once we've found a file ID on the right, count how large it is.
            count = 1
            while disk[right - 1] == id:
                right -= 1
                count += 1
            # print(f"id count: {id} {count}")

            no_space = True
            empty_count = 0
            left = 0

            # Start counting empty spaces on the left.
            while (left < right):
                # If you encounter a non-empty space, reset the counter
                if disk[left] != '.':
                    empty_count = 0
                else:
                    empty_count += 1

                # print(f"empty count {empty_count}")

                left += 1
                # If your empty space count is equal to the size of the file,
                # start replacing empty spaces with the file IDs
                if count == empty_count:
                    # print("match!")
                    temp = left - count
                    while (temp < left):
                        disk[temp] = id
                        temp += 1
                    temp = right
                    while (temp < right + count):
                        disk[temp] = '.'
                        temp += 1
                    no_space = False
                    # print("done moving: ")
                    # print(disk)
                    break

            if no_space:
                # print("skipping!")
                right -= 1

    return disk

def part_one(disk: list[str]) -> int:
    compacted = compact_disk(disk)
    checksum = calculate_checksum(compacted)

    return checksum

def part_two(disk: list[str]) -> int:
    # print(disk)
    compacted = compact_disk_without_fragmentation(disk)
    # print(disk)
    checksum = calculate_checksum(compacted)
    return checksum

if __name__ == "__main__":
    disk = read_disk("input.txt")
    result = part_one(disk)
    print(result)

    disk = read_disk("input.txt")
    result = part_two(disk)
    print(result)
