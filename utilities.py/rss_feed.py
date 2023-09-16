"""generate RSS feed for all blog posts"""

from datetime import datetime
from feedendum import Feed, FeedItem, utils

# from feedendum import to_atom_string
import lxml.etree as ET
from bs4 import BeautifulSoup

SUMMARY_TITLE = "alifeee's blog"
SUMMARY_LINK = "https://blog.alifeee.co.uk"
SUMMARY_AUTHOR = "alifeee"
SUMMARY_ID = "https://blog.alifeee.co.uk"
SUMMARY_ICON = "https://blog.alifeee.co.uk/og-image.png"

# get all li from <ul class="blog posts"> in root index.html
with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
posts_html = soup.find("ul", class_="blog posts").find_all("li")

posts = []
for post in posts_html:
    relative_url = post.find("a", class_="link")["href"]
    date_str = post.find("time")["datetime"]
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date = date.replace(tzinfo=datetime.utcnow().astimezone().tzinfo)
    posts.append(
        {
            "relative_url": relative_url,
            "date": date,
        }
    )

# for each post, open the index.html file in the post directory
#  and get the og fields
for post in posts:
    index_path = f"{post['relative_url']}/index.html"
    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    post["title"] = soup.find("meta", property="og:title")["content"]
    post["description"] = soup.find("meta", property="og:description")["content"]

# make feed items
feed_items = []
for post in posts:
    link = SUMMARY_LINK + "/" + post["relative_url"].lstrip("./")
    feed_items.append(
        FeedItem(
            title=post["title"],
            id=link,
            content=post["description"],
            content_type="html",
            url=link,
            update=post["date"],
        )
    )

# make feed
feed = Feed(
    title=SUMMARY_TITLE,
    url=SUMMARY_LINK,
    description="alifeee's blog",
    items=feed_items,
    update=max(post["date"] for post in posts),
)
Feed.id = SUMMARY_ID


# edit (redefine) library function to_atom_string
def to_atom_string(feed) -> str:
    """Returns a string Atom rappresentation of a feed."""
    nsmap = {None: utils.NS["atom"]}
    schema = f"{{{utils.NS['atom']}}}"
    root = ET.Element(f"{schema}feed", nsmap=nsmap)
    utils.add_text_element(root, f"{schema}title", feed.title)
    utils.add_text_element(root, f"{schema}subtitle", feed.description)
    utils.add_text_element(root, f"{schema}updated", feed.update, datetime.isoformat)
    if feed.url:
        elink = ET.SubElement(root, f"{schema}link")
        elink.set("href", feed.url)
        utils.add_text_element(root, f"{schema}id", feed.url)
    utils.dict_append_etree(feed._data, root)
    for fitem in feed.items:
        entry = ET.SubElement(root, f"{schema}entry")
        utils.add_text_element(entry, f"{schema}title", fitem.title)
        utils.add_text_element(entry, f"{schema}id", fitem.id)
        utils.add_text_element(
            entry, f"{schema}updated", fitem.update, datetime.isoformat
        )
        if fitem.url:
            elink = ET.SubElement(entry, f"{schema}link")
            elink.set("href", fitem.url)
        elem = utils.add_content_element(entry, f"{schema}content", fitem.content)
        utils.set_attribute(elem, "type", fitem.content_type)
        for fcategory in fitem.categories:
            elink = ET.SubElement(entry, f"{schema}category")
            elink.set("term", fcategory)
        utils.dict_append_etree(fitem._data, entry)
    ET.cleanup_namespaces(root)
    return ET.tostring(root, encoding="UTF-8", xml_declaration=True).decode("utf-8")


# save to root feed.xml
with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(to_atom_string(feed))
