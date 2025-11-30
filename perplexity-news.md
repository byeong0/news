---
layout: page
title: Perplexity News
permalink: /perplexity-news/
---

<div class="news-list">
  {% assign perplexity_posts = site.categories.perplexity | where_exp: "item", "item.path contains 'perplexity/ai_news'" %}
  {% for post in perplexity_posts %}
    <article class="news-item">
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <div class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</div>
      <div class="post-excerpt">
        {{ post.excerpt | strip_html | truncatewords: 30 }}
      </div>
    </article>
  {% endfor %}
</div>
