def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    total_strengths = get_total_strengths(lines)
    print(total_strengths)


def get_total_strengths(lines: list[str]) -> int:
    total_strengths = 0
    cycle = 1
    line_no = 0
    x_register = 1
    while line_no < len(lines):
        if is_interesting_cycle(cycle):
            total_strengths += cycle * x_register

        input_line = lines[line_no]
        if input_line.startswith("addx"):
            cycle += 1
            if is_interesting_cycle(cycle):
                total_strengths += cycle * x_register
            _, val = input_line.split()
            x_register += int(val)

        cycle += 1
        line_no += 1

    return total_strengths


def is_interesting_cycle(cycle: int):
    return (cycle - 20) % 40 == 0


main()
