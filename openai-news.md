---
layout: page
title: OpenAI News
permalink: /openai-news/
---

<div class="posts-list">
  {% assign sorted_posts = site.posts | where_exp: "item", "item.path contains 'openai/ai_news'" | sort: 'date' | reverse %}
  {% for post in sorted_posts %}
    <div class="post-item">
      <h3 class="post-title">
        <a href="{{ post.url | absolute_url }}">{{ post.title }}</a>
      </h3>
      <span class="post-date">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      <a href="{{ post.url | absolute_url }}" class="read-more">더 읽기</a>
    </div>
    {% unless forloop.last %}
      <hr>
    {% endunless %}
  {% endfor %}
  
  {% if sorted_posts.size == 0 %}
    <p>아직 게시물이 없습니다.</p>
  {% endif %}
</div>

<style>
  .post-item {
    margin-bottom: 20px;
  }
  .post-title {
    margin-bottom: 5px;
  }
  .post-date {
    display: block;
    color: #9a9a9a;
    margin-bottom: 10px;
  }
  .post-excerpt {
    margin-bottom: 10px;
  }
  .read-more {
    display: inline-block;
    margin-top: 5px;
    font-weight: bold;
  }
</style>
