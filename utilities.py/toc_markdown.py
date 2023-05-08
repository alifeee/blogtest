# generates a table of contents for a markdown file immediately after the first header

import re
import sys


def toc_markdown(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    all_text = "".join(lines)

    if '<div class="toc">' in all_text:
        print("Table of contents already exists in file.")
        sys.exit(1)

    # find all headers (## or more)
    headers = re.findall(
        r"^##+\s.*$",
        all_text,
        re.MULTILINE,
    )

    # generate toc
    table_of_contents = "\n"
    table_of_contents += '<div class="toc">\n\n'
    for header in headers:
        depth = len(re.findall(r"^#+", header)[0])
        title = re.findall(r"^#+\s(.*)$", header)[0]
        link = title.lower().replace(" ", "-")
        link = re.sub(r"[^a-zA-Z0-9-]", "", link)
        list_prefix = "    " * (depth - 2) + "1. "
        table_of_contents += f"{list_prefix}[{title}](#{link})"
        table_of_contents += "\n\n"
    table_of_contents += "</div>\n"

    lines.insert(1, table_of_contents)

    with open(filename, "w") as f:
        f.writelines(lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python toc_markdown.py <filename>")
        sys.exit(1)
    toc_markdown(sys.argv[1])


if __name__ == "__main__":
    main()
