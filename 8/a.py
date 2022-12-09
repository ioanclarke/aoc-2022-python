def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    grid: list[list[int]] = [list(map(int, list(line))) for line in lines]

    visible_tree_count = 0
    for row_num, row in enumerate(grid):
        for tree_num in range(len(row)):
            # Check if tree is on an edge
            if is_on_edge(grid, row_num, tree_num):
                visible_tree_count += 1
            elif is_visible_from_outside(grid, row_num, tree_num):
                visible_tree_count += 1

    print(visible_tree_count)


def is_on_edge(grid: list[list[int]], row_num: int, tree_num: int):
    return row_num in (0, len(grid) - 1) or tree_num in (0, len(grid[0]) - 1)


def is_visible_from_top(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> bool:
    return not any(grid[n][tree_num] >= height for n in range(row_num))


def is_visible_from_right(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> bool:
    return not any(
        grid[row_num][n] >= height for n in range(tree_num + 1, len(grid[0]))
    )


def is_visible_from_bottom(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> bool:
    return not any(grid[n][tree_num] >= height for n in range(row_num + 1, len(grid)))


def is_visible_from_left(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> bool:
    return not any(grid[row_num][n] >= height for n in range(tree_num))


def is_visible_from_outside(grid: list[list[int]], row_num: int, tree_num: int) -> bool:
    height = grid[row_num][tree_num]
    return (
        is_visible_from_top(grid, row_num, tree_num, height)
        or is_visible_from_right(grid, row_num, tree_num, height)
        or is_visible_from_bottom(grid, row_num, tree_num, height)
        or is_visible_from_left(grid, row_num, tree_num, height)
    )


main()
