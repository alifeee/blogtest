"""Parses all "current" blog posts and returns them as a Python object
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List

# pip install tzdata, beautifulsoup4
from zoneinfo import ZoneInfo  # timezone
from bs4 import BeautifulSoup

INDEX_FILE = "index.html"


@dataclass
class Post:
    """A dataclass to hold a blog post"""

    title: str
    description: str
    relative_url: str
    date: datetime


def get_all_posts() -> List[Post]:
    with open(INDEX_FILE, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    posts_html = soup.find("ul", class_="blog posts").find_all("li", recursive=False)

    posts = []
    for post in posts_html:
        relative_url = post.find("a", class_="link")["href"]
        date_str = post.find("time")["datetime"]
        date = datetime.strptime(date_str, "%Y-%m-%d")
        date = date.replace(tzinfo=ZoneInfo("Etc/UTC"))

        index_path = f"{relative_url}/index.html"
        with open(index_path, "r", encoding="utf-8") as file:
            post_soup = BeautifulSoup(file, "html.parser")
        title = post_soup.find("meta", property="og:title")["content"]
        description = post_soup.find("meta", property="og:description")["content"]

        posts.append(
            Post(
                title=title,
                description=description,
                relative_url=relative_url,
                date=date,
            )
        )

    posts.sort(key=lambda x: x.date, reverse=True)
    return posts


if __name__ == "__main__":
    print("getting posts...")
    ps = get_all_posts()
    print("posts:")
    for p in ps:
        print(p)
