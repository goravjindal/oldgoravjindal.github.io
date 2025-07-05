---
layout: page
title: "CS Theory RSS"
nav: true
nav_order: 6
permalink: /cstheoryrss/
---

{% if page.title == "CS Theory RSS" %}

# CS Theory RSS Posts (last 6 months), from [https://theory.report/atom.xml](https://theory.report/atom.xml)

<input type="text" id="search-box" placeholder="Search posts..." style="margin-bottom: 1em; width: 100%; padding: 0.5em; font-size: 1em;">

{% assign sorted_posts = site.cstheoryrss | sort: 'date' | reverse %}


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
  <p>No posts found in CS Theory RSS.</p>
{% endif %}

<script src="https://unpkg.com/lunr/lunr.js"></script>
<script>
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
    this.field('title', {boost: 10})
    this.field('content')

    posts.forEach(function (doc) {
      this.add(doc)
    }, this)
  });

  const searchBox = document.getElementById('search-box');
  const postsList = document.getElementById('posts-list');

  function renderPosts(postsArray) {
    if (postsArray.length === 0) {
      postsList.innerHTML = '<li>No results found</li>';
      return;
    }
    postsList.innerHTML = postsArray.map(p => {
      if (p.url) {
        return `<li><a href="${p.url}">${p.title}</a> — <small></small></li>`;
      } else {
        const post = posts.find(post => post.url === p.ref);
        if (post) {
          return `<li><a href="${post.url}">${post.title}</a></li>`;
        }
        return '';
      }
    }).join('');
  }

  renderPosts(posts);

  searchBox.addEventListener('input', function () {
    let query = this.value.trim().toLowerCase();

    if (query === "") {
      renderPosts(posts);
      return;
    }

    let results = idx.search(query);
    if (results.length === 0) {
      const wildcardQuery = query.split(/\s+/).map(term => term + '*').join(' ');
      results = idx.search(wildcardQuery);
    }

    renderPosts(results);
  });
</script>

{% endif %}

