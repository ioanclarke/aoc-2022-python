from __future__ import annotations

from typing import NamedTuple


class File(NamedTuple):
    path: str
    size: int


class SizedDir(NamedTuple):
    path: str
    size: int


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    dirs, files = parse_input(lines)

    sized_dirs = find_dir_sizes(dirs, files)
    root = next(d for d in sized_dirs if d.path == "/")
    total_disk_space = 70_000_000
    space_required_for_update = 30_000_000
    available_space = total_disk_space - root.size
    need_to_delete = space_required_for_update - available_space

    sized_dirs = sorted(list(sized_dirs), key=lambda d: d.size)
    deletable = next(d for d in sized_dirs if d.size >= need_to_delete)
    print(deletable.size)


def parse_input(lines: list[str]) -> tuple[set[str], set[File]]:
    files = set()
    dirs = {"/"}
    curr_dir = "/"
    # skip initial 'cd /' line
    line_no = 1
    while line_no < len(lines):
        input_line = lines[line_no]
        if input_line.startswith("$ cd"):
            command = input_line.split()
            arg = command[2]
            if arg == "..":
                curr_dir = curr_dir[: curr_dir.rfind("/")]
                curr_dir = curr_dir[: curr_dir.rfind("/")]
                curr_dir += "/"
            else:
                curr_dir += arg + "/"

        # This means the input_line is a dir or file
        elif not input_line.startswith("$ ls"):
            entry = input_line.split()
            if entry[0] != "dir":
                file = File(curr_dir + entry[1], int(entry[0]))
                files.add(file)
            else:
                dirs.add(curr_dir + entry[1])

        line_no += 1

    return dirs, files


def find_dir_sizes(dirs: set[str], files: set[File]) -> set[SizedDir]:
    return {get_size(dir_name, files) for dir_name in dirs}


def get_size(dir_name: str, files: set[File]) -> SizedDir:
    return SizedDir(dir_name, sum(file.size for file in files if dir_name in file.path))


main()
