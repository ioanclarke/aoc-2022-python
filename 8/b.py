def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    grid: list[list[int]] = [list(map(int, list(line))) for line in lines]

    grid_height = len(grid)
    grid_width = len(grid[0])
    scenic_scores = []
    for row_num in range(grid_height):
        for tree_num in range(grid_width):
            scenic_scores.append(
                0
                if is_on_edge(grid, row_num, tree_num)
                else scenic_score(grid, row_num, tree_num)
            )

    highest_scenic_score = max(scenic_scores)
    print(highest_scenic_score)


def is_on_edge(grid: list[list[int]], row_num: int, tree_num: int):
    return row_num in (0, len(grid) - 1) or tree_num in (0, len(grid[0]) - 1)


def top_view_distance(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> int:
    count = 1
    for n in range(row_num - 1, -1, -1):
        if grid[n][tree_num] < height and not is_on_edge(grid, n, tree_num):
            count += 1
        else:
            break
    return count


def right_view_distance(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> int:
    count = 1
    for n in range(tree_num + 1, len(grid[0])):
        if grid[row_num][n] < height and not is_on_edge(grid, n, tree_num):
            count += 1
        else:
            break
    return count


def bottom_view_distance(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> int:
    count = 1
    for n in range(row_num + 1, len(grid)):
        if grid[n][tree_num] < height and not is_on_edge(grid, n, tree_num):
            count += 1
        else:
            break
    return count


def left_view_distance(
    grid: list[list[int]], row_num: int, tree_num: int, height: int
) -> int:
    count = 1
    for n in range(tree_num - 1, -1, -1):
        if grid[row_num][n] < height and not is_on_edge(grid, n, tree_num):
            count += 1
        else:
            break
    return count


def scenic_score(grid: list[list[int]], row_num: int, tree_num: int) -> int:
    height = grid[row_num][tree_num]
    return (
        top_view_distance(grid, row_num, tree_num, height)
        * right_view_distance(grid, row_num, tree_num, height)
        * bottom_view_distance(grid, row_num, tree_num, height)
        * left_view_distance(grid, row_num, tree_num, height)
    )


main()
