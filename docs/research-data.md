# Research Data

<div class="grid cards" markdown>

{% for r in all_resources_sorted() %}

- **[{{ r.title }}]({{ r.url }})**  

    {{ r.description }}

    {% if r.paper_title %}**Paper:** [{{ r.paper_title }}]({{ r.paper_url }})  {% endif %}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}

</div>
