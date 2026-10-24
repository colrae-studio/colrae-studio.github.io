"""Fill {{ contact_url }} from extra.contact_url in mkdocs.yml."""


def on_page_markdown(markdown, config, **kwargs):
    url = config.extra.get("contact_url", "")
    return markdown.replace("{{ contact_url }}", url)
