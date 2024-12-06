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

def part2(program: str) -> int:
    # I was going to try to use fancy regex to parse the entire thing all at
    # once but I gave up because I'm bad at regex.
    result = 0
    mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    do = r"do\(\)"
    dont = r"don't\(\)"
    do_flag = True
    index = 0
    while index < len(program):
        # The longest an instruction can be is mul(000,000) so look ahead 12 characters.
        look_ahead = program[index:index+12]
        for match in re.findall(mul, look_ahead):
            if do_flag:
                lhs, rhs = map(int, match)
                result += lhs * rhs
                index += 5 # Jump ahead 5 to prevent double-count

        if re.match(dont, look_ahead):
            do_flag = False
        elif re.match(do, look_ahead):
            do_flag = True
        index += 1

    return result

if __name__=="__main__":
    program = read_program("input.txt")
    result = part1(program)
    print(result)
    result = part2(program)
    print(result)