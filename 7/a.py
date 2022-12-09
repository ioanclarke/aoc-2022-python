from __future__ import annotations

from dataclasses import dataclass

with open("test.txt") as f:
    lines = f.read().splitlines()

# watch out for doing ls twice in the same directory


tree = {}


@dataclass
class File:
    name: str
    size: int

    def of(self, ):


@dataclass
class Dir:
    name: str
    child_files: list[File]
    child_dirs: list[Dir]

    def add_child_file(self, file: File):
        self.child_files.append(file)

    def add_child_dir(self, direc: Dir):
        self.child_dirs.append(direc)


# We know input_line starts with '$cd'
def get_new_cwd(input_line: str):
    return input_line.split()[2]


def main():
    dirs: dict[str, Dir] = {}
    curr_dir = "/"
    # skip initial 'cd /' line
    line_no = 1
    while line_no < len(lines):
        input_line = lines[line_no]
        print(f"{input_line=}")
        print(f"{curr_dir=}")
        if input_line.startswith("$ ls"):
            continue
        elif input_line.startswith("$ cd"):
            curr_dir = get_new_cwd(input_line)
        else:
            entry = input_line.split()
            if entry[0] == "dir":





            direc = dirs.get(curr_dir, Dir(curr_dir, [], []))
            file = get_new_f
            curr_file = File()
            direc.add_child_file()

        line_no += 1


main()
# print(f"Processing line >>> {input_line}")
# if input_line == "$ ls":
#     line_no += 1
#     output_lines = []
#     while line_no < len(lines):
#         output_line = lines[line_no]
#         print(f"Processing output line >>> {output_line}")
#         if output_line.startswith("$"):
#             break
#         else:
#             output_lines.append(output_line)
#             line_no += 1
#     print(f"Processing ls output: {output_lines}")
