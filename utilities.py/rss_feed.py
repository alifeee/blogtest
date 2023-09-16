"""generate RSS feed for all blog posts"""

from datetime import datetime
from feedendum import Feed, FeedItem, to_atom_string
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

# save to root feed.xml
with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(to_atom_string(feed))
