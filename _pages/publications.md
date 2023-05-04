---
layout: page
permalink: /publications/
title: Publications
years: [2023, 2021, 2020, 2019, 2018, 2017,2014, 2013, 2012, 2008]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
