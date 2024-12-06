def read_rules(filename: str) -> dict[int, tuple[set[int], set[int]]]:
    rules = {}
    with open(filename, 'r') as file:
        for line in file:
            if '|' in line:
                left, right = map(int, line.split('|'))

                # Initialize rules for new numbers.
                if left not in rules:
                    rules[left] = (set(), set())
                if right not in rules:
                    rules[right] = (set(), set())

                # The left number gets its right rules updated.
                left_rules = rules.get(left)
                left_rules[1].add(right)

                # The right number gets its left rules updated.
                right_rules = rules.get(right)
                right_rules[0].add(left)

    return rules

def read_updates(filename: str) -> list[list[int]]:
    updates = []
    with open(filename, 'r') as file:
        for line in file:
            if ',' in line:
                update = [int(num) for num in line.strip().split(',')]
                updates.append(update)

    return updates

def check_rules(nums: list[int], excluded: set[int]):
    for num in nums:
        if num in excluded:
            return False

    return True

def get_correctly_ordered_updates(rules, updates) -> list[list[int]]:
    correctly_ordered_updates = []
    for update in updates:
        is_correctly_ordered = True

        for index, num in enumerate(update):
            preceeding_nums, following_nums = rules[num]
            good_preceeding = check_rules(update[:index], following_nums)
            good_following = check_rules(update[index:], preceeding_nums)
            if not good_preceeding or not good_following:
                is_correctly_ordered = False
                break # No need to keep checking.

        if is_correctly_ordered:
            correctly_ordered_updates.append(update)

    return correctly_ordered_updates

def get_incorrectly_ordered_updates(rules, updates) -> list[list[int]]:
    incorrectly_ordered_updates = []
    for update in updates:
        is_correctly_ordered = True

        for index, num in enumerate(update):
            preceeding_nums, following_nums = rules[num]
            good_preceeding = check_rules(update[:index], following_nums)
            good_following = check_rules(update[index:], preceeding_nums)
            if not good_preceeding or not good_following:
                is_correctly_ordered = False
                break # No need to keep checking.

        if not is_correctly_ordered:
            incorrectly_ordered_updates.append(update)

    return incorrectly_ordered_updates

def get_middle_number_sum(updates: list[list[int]]) -> int:
    sum = 0
    for update in updates:
        middle_index = (len(update) // 2)
        sum += update[middle_index]

    return sum

def part_one(rules, updates) -> int:
    correctly_ordered_updates = get_correctly_ordered_updates(rules, updates)
    middle_number_sum = get_middle_number_sum(correctly_ordered_updates)

    return middle_number_sum

if __name__=="__main__":
    rules = read_rules("sample.txt")
    updates = read_updates("sample.txt")
    result = part_one(rules, updates)
    print(result)
    incorrect_updates = get_incorrectly_ordered_updates(rules, updates)
    print(incorrect_updates)