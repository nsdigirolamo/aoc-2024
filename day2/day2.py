def read_reports(filename: str) -> list[list[int]]:
    reports = []
    with open(filename, 'r') as file:
        for line in file:
            levels = [int(level) for level in line.strip().split()]
            reports.append(levels)
    return reports

def is_report_safe(report: list[int]) -> bool:
    last_change = 0
    is_safe = True
    for i in range(len(report)):
        if i + 1 < len(report):
            change = report[i] - report[i + 1]
            bad_rate = abs(change) == 0 or 3 < abs(change)
            bad_direction = last_change != 0 and ((change < 0) != (last_change < 0))
            is_safe = not (bad_rate or bad_direction) and is_safe
            last_change = change
    return is_safe

def part1(reports: list[list[int]]) -> int:
    safe_count = 0
    for report in reports:
        safe_count += is_report_safe(report)
    return safe_count

def part2(reports: list[list[int]]) -> int:
    safe_count = 0
    for report in reports:
        is_safe = is_report_safe(report)
        if not is_safe:
            for i in range(len(report)): # lazy solution lol
                if is_report_safe(report[0:i] + report[i+1:]):
                    is_safe = True
        safe_count += is_safe
    return safe_count

if __name__=="__main__":
    reports = read_reports("input.txt")
    safe_count = part1(reports)
    print(safe_count)
    safe_count = part2(reports)
    print(safe_count)
