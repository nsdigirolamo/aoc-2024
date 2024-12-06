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
        middle_index = len(update) // 2
        sum += update[middle_index]

    return sum

def reorder_update(rules, update: list[int]) -> list[int]:
    reordered_update = [0] * len(update)
    for num1 in update:
        preceeding_nums, _ = rules[num1]
        preceed_count = 0
        # Start counting the number of elements that must preceed num1.
        for num2 in update:
            if num2 in preceeding_nums:
                preceed_count += 1
        # The preceed count is num1's new position.
        reordered_update[preceed_count] = num1

    return reordered_update

def part_one(rules, updates) -> int:
    correctly_ordered_updates = get_correctly_ordered_updates(rules, updates)
    middle_number_sum = get_middle_number_sum(correctly_ordered_updates)

    return middle_number_sum

def part_two(rules, updates) -> int:
    incorrectly_ordered_updates = get_incorrectly_ordered_updates(rules, updates)
    reordered_updates = []
    for update in incorrectly_ordered_updates:
        reordered_update = reorder_update(rules, update)
        reordered_updates.append(reordered_update)
    middle_number_sum = get_middle_number_sum(reordered_updates)

    return middle_number_sum

if __name__=="__main__":
    rules = read_rules("input.txt")
    updates = read_updates("input.txt")
    result = part_one(rules, updates)
    print(result)
    result = part_two(rules, updates)
    print(result)
