"""generate RSS feed for all blog posts"""

from feedendum import Feed, FeedItem, to_atom_string
from bs4 import BeautifulSoup

# get all li from <ul class="blog posts"> in root index.html
with open("index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

posts_html = soup.find("ul", class_="blog posts").find_all("li")

posts = []
for post in posts_html:
    title: str = post.find("h2", class_="title").text
    title_lines = title.split("\n")
    title = " ".join([line.strip() for line in title_lines]).strip()

    relative_url = post.find("a", class_="link")["href"]
    date = post.find("time")["datetime"]
    posts.append(
        {
            "title": title,
            "relative_url": relative_url,
            "date": date,
        }
    )

print(posts)
