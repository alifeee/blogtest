# generates a table of contents for a markdown file immediately after the first header

import re
import sys

CONTENTS_TITLE = "Contents"


def toc_markdown(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    all_text = "".join(lines)

    # if "## Contents" exists anywhere in the file
    if f"## {CONTENTS_TITLE}" in all_text:
        print("Table of contents already exists in file.")
        sys.exit(1)

    if lines[2][0] == "-":
        print("Table of contents already exists in file.")
        sys.exit(1)

    # find all headers (## or more)
    headers = re.findall(
        r"^##+\s.*$",
        all_text,
        re.MULTILINE,
    )

    # toc = f"\n## {CONTENTS_TITLE}\n\n"
    toc = "\n"
    for header in headers:
        depth = len(re.findall(r"^#+", header)[0])
        title = re.findall(r"^#+\s(.*)$", header)[0]
        toc += (
            f"{'  ' * (depth - 2)}- [{title}](#{title.lower().replace(' ', '-')})\n\n"
        )

    # insert toc
    del lines[1]
    lines.insert(1, toc)

    for line in lines:
        print(line, end="")

    with open(filename, "w") as f:
        f.writelines(lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python toc_markdown.py <filename>")
        sys.exit(1)
    toc_markdown(sys.argv[1])


if __name__ == "__main__":
    main()
