def find_marker_pos(stream: str, unique_req: int) -> int:
    queue = list(stream[:unique_req])

    if all_distinct(queue):
        return unique_req

    for idx, ch in enumerate(stream[unique_req:], unique_req + 1):
        queue.pop(0)
        queue.append(ch)
        if all_distinct(queue):
            return idx


def all_distinct(lst: list[str]):
    return len(set(lst)) == len(lst)


def main():
    unique_req = 14
    with open("input.txt") as f:
        stream = f.read()

    pos = find_marker_pos(stream, unique_req)

    print(pos)


main()
