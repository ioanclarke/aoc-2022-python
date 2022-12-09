from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple


# watch out for doing ls twice in the same directory


class File(NamedTuple):
    path: str
    size: int


class SizedDir(NamedTuple):
    path: str
    size: int
    # child_files: list[File]
    # child_dirs: list[Dir]
    #
    # def add_child_file(self, file: File):
    #     self.child_files.append(file)
    #
    # def add_child_dir(self, direc: Dir):
    #     self.child_dirs.append(direc)


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    dirs, files = parse_input(lines)
    # print(f"{files=}")
    # print("\n"*10)
    # print(f"{dirs=}")
    # print(f"{len(dirs)=}")

    sized_dirs = find_dir_sizes(dirs, files)
    # print(f"{sized_dirs=}")
    total_size_of_small_dirs = sum(direc.size for direc in sized_dirs if direc.size <= 100_000)
    # print("\n"*10)
    # print([direc for direc in sized_dirs if direc.size <= 100_000])
    print(total_size_of_small_dirs)


def parse_input(lines: list[str]) -> tuple[set[str], set[File]]:
    files = set()
    dirs = set()
    curr_dir = "/"
    # skip initial 'cd /' line
    line_no = 1
    while line_no < len(lines):
        input_line = lines[line_no]
        # print(f"{input_line=}")
        # print(f"{curr_dir=}")
        if input_line.startswith("$ cd"):
            command = input_line.split()
            arg = command[2]
            if arg == "..":
                curr_dir = curr_dir[:curr_dir.rfind("/")]
                curr_dir = curr_dir[:curr_dir.rfind("/")]
                curr_dir += "/"
                # print(f"found '..' as arg to cd. changing curr_dir to {curr_dir}")
            else:
                curr_dir += arg + "/"
                # print(f"found {arg} as arg to cd. changing curr_dir to {curr_dir}")

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
    size = 0
    for file in files:
        if dir_name in file.path:
            # print(f"file {file} contains {dir_name}. adding {file.size} to sum")
            size += file.size
    return SizedDir(dir_name, size)


# 517524 too low
main()
