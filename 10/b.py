from typing import TypeAlias

Image: TypeAlias = list[list[str]]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    image = generate_image(lines)
    for row in image:
        print("".join(row))


def generate_image(lines: list[str]) -> Image:
    image: list[list[str]] = [["." for _ in range(40)] for _ in range(6)]
    cycle = 1
    line_no = 0
    sprite_middle_pos = 1

    while line_no < len(lines):
        image = update_image(image, cycle, sprite_middle_pos)
        input_line = lines[line_no]
        if input_line.startswith("addx"):
            cycle += 1
            image = update_image(image, cycle, sprite_middle_pos)
            _, val = input_line.split()
            sprite_middle_pos += int(val)

        cycle += 1
        line_no += 1

    return image


def update_image(image: Image, cycle: int, sprite_middle_pos: int) -> Image:
    draw_pos_y, draw_pos_x = divmod(cycle - 1, 40)
    if draw_pos_x - 1 <= sprite_middle_pos <= draw_pos_x + 1:
        image[draw_pos_y][draw_pos_x] = "#"
    return image


main()
