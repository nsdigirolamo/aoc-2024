def read_equations(filename: str) -> list[tuple[int, list[int]]]:
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            equation = line.strip().split(":")
            test_value = int(equation[0])
            operators = list(map(int, equation[1].strip().split(" ")))
            equations.append((test_value, operators))

    return equations

def find_possible_results(nums: list[int]) -> list[int]:
    results = []
    local = nums[-1]

    if len(nums) == 1:
        results.append(local)
        print(nums)
    else:
        for result in find_possible_results(nums[:-1]):
            results.append(result + local)
            results.append(result * local)

    return results

def part_one(equations: list[tuple[int, list[int]]]) -> int:
    sum = 0
    for test_value, nums in equations:
        results = set(find_possible_results(nums))
        if test_value in results:
            sum += test_value

    return sum

if __name__ == "__main__":
    equations = read_equations("input.txt")
    result = part_one(equations)
    print(result)
