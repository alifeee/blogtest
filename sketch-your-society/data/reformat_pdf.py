"""takes the raw pdf and crops it, maybe some other stuff"""
import os

# 3.10.0
from pypdf import PdfReader, PdfWriter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

reader = PdfReader(f"{__location__}/freshers-fair-book-scan.pdf")
writer = PdfWriter()

total_pages = len(reader.pages)

for i, page in enumerate(reader.pages):
    # lower right to right/2, top/2 gets "top right"
    # lower left to right/2, top/2 gets "top right"
    if i == 0:
        print("bottom", page.mediabox.bottom)
        print("left", page.mediabox.left)
        print("top", page.mediabox.top)
        print("right", page.mediabox.right)
        print("lower left", page.mediabox.lower_left)
        print("lower right", page.mediabox.lower_right)
        page.mediabox.lower_right = (
            page.mediabox.right / 2,
            page.mediabox.top / 2,
        )
        writer.add_page(page)
        continue
    elif i == total_pages - 1:
        page.mediabox.lower_left = (
            page.mediabox.right / 2,
            page.mediabox.top / 2,
        )
        writer.add_page(page)
        continue
    # copy page to 2 pages
    writer.add_page(page)
    writer.add_page(page)

    page1 = writer.pages[-2]
    page2 = writer.pages[-1]
    page1.mediabox.lower_left = (
        page1.mediabox.right / 2,
        page1.mediabox.top / 2,
    )
    page2.mediabox.upper_left = (
        page2.mediabox.right / 2,
        page2.mediabox.top / 2,
    )

with open(f"{__location__}/freshers-fair-book-cropped.pdf", "wb") as fp:
    writer.write(fp)
