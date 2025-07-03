---
layout: page
title: "CS Theory RSS"
permalink: /cstheoryrss/
---

# CS Theory RSS Posts (last 1 year)

<input type="text" id="search-box" placeholder="Search posts..." style="margin-bottom: 1em; width: 100%; padding: 0.5em; font-size: 1em;">

{% assign sorted_posts = site.posts | where_exp: "post", "post.path contains '_posts/cstheoryrss'" | sort: 'date' | reverse %}

{% if sorted_posts.size > 0 %}
  <ul id="posts-list">
    {% for post in sorted_posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a> — <small>{{ post.date | date: "%Y-%m-%d" }}</small>
        <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
      </li>
    {% endfor %}
  </ul>
{% else %}
  <p>No posts found in _posts/cstheoryrss.</p>
{% endif %}

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script>
  // Build a simple Lunr index for client-side search
  const posts = [
    {% for post in sorted_posts %}
    {
      "title": {{ post.title | jsonify }},
      "url": {{ post.url | jsonify }},
      "content": {{ post.content | strip_html | jsonify }}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  const idx = lunr(function () {
    this.ref('url')
    this.field('title')
    this.field('content')

    posts.forEach(function (doc) {
      this.add(doc)
    }, this)
  });

  const searchBox = document.getElementById('search-box');
  const postsList = document.getElementById('posts-list');

  searchBox.addEventListener('input', function () {
    const query = this.value.trim();
    if (query === "") {
      // Show all posts
      postsList.innerHTML = posts.map(p => 
        `<li><a href="${p.url}">${p.title}</a> — <small></small></li>`).join('');
      return;
    }
    const results = idx.search(query);
    if (results.length === 0) {
      postsList.innerHTML = '<li>No results found</li>';
      return;
    }
    postsList.innerHTML = results.map(r => {
      const post = posts.find(p => p.url === r.ref);
      return `<li><a href="${post.url}">${post.title}</a></li>`;
    }).join('');
  });
</script>

