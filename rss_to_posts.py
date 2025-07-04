import os
import feedparser
from datetime import datetime, timedelta
import markdownify

RSS_URL = "https://theory.report/atom.xml"
POSTS_DIR = "_posts/cstheoryrss"
ONE_YEAR_AGO = datetime.utcnow() - timedelta(days=365)

os.makedirs(POSTS_DIR, exist_ok=True)

def sanitize_filename(title):
    # simple slugify: lowercase, replace spaces & special chars with hyphen
    import re
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return slug or "post"

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

        if published < ONE_YEAR_AGO:
            continue  # skip older than 1 year

        date_prefix = published.strftime("%Y-%m-%d")
        slug = sanitize_filename(entry.title)
        filename = f"{date_prefix}-{slug}.md"
        filepath = os.path.join(POSTS_DIR, filename)

        # Skip if file exists to avoid rewriting
        if os.path.exists(filepath):
            continue

        content_html = entry.summary if hasattr(entry, "summary") else ""
        content_md = markdownify.markdownify(content_html, heading_style="ATX")

        front_matter = f"---\nlayout: post\ncategory: cstheoryrss\ntitle: \"{entry.title}\"\ndate: {published.isoformat()}\n---\n\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(front_matter)
            f.write(content_md)

        count += 1

    print(f"Saved {count} posts from the last year.")

if __name__ == "__main__":
    fetch_and_save()

