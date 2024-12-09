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

    if disk[right] == '.' and disk[left] != '.':
        disk[right] = disk[left]
        disk[left] = '.'

    return disk

def part_one(disk: list[int]) -> int:
    compacted = compact_disk(disk)
    checksum = calculate_checksum(compacted)

    return checksum

if __name__ == "__main__":
    disk = read_disk("input.txt")
    result = part_one(disk)
    print(result)
