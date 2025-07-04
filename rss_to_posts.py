import os
import feedparser
from datetime import datetime, timedelta
import markdownify
import re

RSS_URL = "https://theory.report/atom.xml"
POSTS_DIR = "_cstheoryrss"
SIX_MONTHS_AGO = datetime.utcnow() - timedelta(days=182)

os.makedirs(POSTS_DIR, exist_ok=True)

def sanitize_filename(title):
    # simple slugify: lowercase, replace spaces & special chars with hyphen
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return slug or "post"

def delete_old_posts():
    for fname in os.listdir(POSTS_DIR):
        match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-.*\.md$', fname)
        if match:
            year, month, day = map(int, match.groups())
            file_date = datetime(year, month, day)
            if file_date < SIX_MONTHS_AGO:
                os.remove(os.path.join(POSTS_DIR, fname))
                print(f"Deleted old post: {fname}")

def fetch_and_save():
    feed = feedparser.parse(RSS_URL)
    count = 0

    for entry in feed.entries:
        published = None
        if hasattr(entry, "published_parsed"):
            published = datetime(*entry.published_parsed[:6])
        elif hasattr(entry, "updated_parsed"):
            published = datetime(*entry.updated_parsed[:6])
        else:
            continue

        if published < SIX_MONTHS_AGO:
            continue  # skip older than 6 months

        date_prefix = published.strftime("%Y-%m-%d")
        slug = sanitize_filename(entry.title)
        filename = f"{date_prefix}-{slug}.md"
        filepath = os.path.join(POSTS_DIR, filename)

        # Skip if file exists to avoid rewriting
        if os.path.exists(filepath):
            continue

        content_html = entry.summary if hasattr(entry, "summary") else ""
        content_md = markdownify.markdownify(content_html, heading_style="ATX")
        front_matter = (
            f"---\n"
            f"layout: post\n"
            f"nav: true\n"
            f"category: cstheoryrss\n"
            f"title: \"{entry.title}\"\n"
            f"date: {published.isoformat()}\n"
            f"---\n\n"
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(front_matter)
            f.write(content_md)
            f.write(f"\n\n[Read original post]({entry.link})\n")

        count += 1

    print(f"Saved {count} posts from the last 6 months.")

if __name__ == "__main__":
    delete_old_posts()
    fetch_and_save()

