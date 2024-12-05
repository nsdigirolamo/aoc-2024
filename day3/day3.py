import re

def read_program(filename: str) -> str:
    program = ""
    with open(filename, 'r') as file:
        for line in file:
            program += line
    return program

def part1(program: str) -> int:
    result = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for match in re.findall(pattern, program):
        lhs, rhs = map(int, match)
        result += lhs * rhs
    return result

if __name__=="__main__":
    program = read_program("input.txt")
    result = part1(program)
    print(result)
    result = part2(program)
    print(result)