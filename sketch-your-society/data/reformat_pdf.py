"""takes the raw pdf and crops it, maybe some other stuff"""
import os

# 3.10.0
from pypdf import PdfReader, PdfWriter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

reader = PdfReader(f"{__location__}/freshers-fair-book-scan.pdf")
writer = PdfWriter()

total_pages = len(reader.pages)

REMOVE_PAGES = [2, 4]

for i, page in enumerate(reader.pages):
    # the pages in the original pdf are rotated, so that...
    # lower right to right/2, top/2 gets "top right"
    # upper right to right/2, top/2 gets "top left"
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
    if i == total_pages - 1:
        page.mediabox.lower_right = (
            page.mediabox.right / 2,
            page.mediabox.top / 2,
        )
        writer.add_page(page)
        continue

    page1_num = i * 2
    if page1_num not in REMOVE_PAGES:
        writer.add_page(page)
        page1 = writer.pages[-1]
        page1.mediabox.upper_right = (
            page1.mediabox.right / 2,
            page1.mediabox.top / 2,
        )

    page2_num = i * 2 + 1
    if page2_num not in REMOVE_PAGES:
        writer.add_page(page)
        page2 = writer.pages[-1]
        page2.mediabox.lower_right = (
            page2.mediabox.right / 2,
            page2.mediabox.top / 2,
        )

for page in writer.pages:
    page.compress_content_streams()

with open(f"{__location__}/freshers-fair-book-cropped.pdf", "wb") as fp:
    writer.write(fp)
