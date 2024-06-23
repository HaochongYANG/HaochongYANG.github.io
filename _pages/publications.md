---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for publication in site.publications %}
  <div class="publication-entry">
    <!-- Title without hyperlink -->
    <h3>{{ publication.title }}</h3>
    <!-- Citation as plain text -->
    <p>{{ publication.citation }}</p>
  </div>
{% endfor %}
