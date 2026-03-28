---
layout: legal
title: Legal
---

# Legal

These pages contain the privacy policy and terms for each project.

{% for project in site.data.legal %}
## {{ project.title }}

- [Privacy Policy](/legal/{{ project.slug }}/privacy-policy)
- [Terms and Conditions](/legal/{{ project.slug }}/terms-and-conditions)

{% endfor %}
