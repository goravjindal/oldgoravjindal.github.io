#!/usr/bin/env python3

import feedparser
from markdownify import markdownify as md
from datetime import datetime
import os
import hashlib
import re

# --- CONFIGURATION ---
RSS_FEED_URL = 'https://example.com/rss'  # Replace with your feed
POST_DIR = '_posts'

def slugify(text):
    return re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', text.lower()))

def get_post_path(date, title):
    slug = slugify(title)[:50]
    return os.path.join(POST_DIR, f'{date.strftime("%Y-%m-%d")}-{slug}.md')

def entry_to_post(entry):
    title = entry.title
    link = entry.link
    pub_date = entry.get('published', '') or entry.get('updated', '')
    try:
        date_obj = datetime(*entry.published_parsed[:6])
    except:
        date_obj = datetime.utcnow()

    content = entry.get('summary', '') or entry.get('content', [{'value': ''}])[0]['value']
    content_md = md(content)

    post_filename = get_post_path(date_obj, title)

    if os.path.exists(post_filename):
        return None  # Skip duplicates

    frontmatter = f"""---
layout: post
title: "{title.replace('"', '\\"')}"
date: {date_obj.strftime("%Y-%m-%d %H:%M:%S %z")}
categories: [rss]
external_link: {link}
---

"""
    full_post = frontmatter + content_md + "\n"
    with open(post_filename, 'w', encoding='utf-8') as f:
        f.write(full_post)
    return post_filename

def main():
    os.makedirs(POST_DIR, exist_ok=True)
    feed = feedparser.parse(RSS_FEED_URL)
    new_posts = []

    for entry in feed.entries:
        result = entry_to_post(entry)
        if result:
            new_posts.append(result)

    print(f"Added {len(new_posts)} new posts.")

if __name__ == '__main__':
    main()

