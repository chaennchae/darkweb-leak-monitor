from urllib.parse import urljoin, urlparse
'''
def extract_onion_links(base_url: str, soup):
    links = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        if ".onion" in href:
            full = urljoin(base_url, href)
            links.add(full)

    return links
'''
def extract_onion_links(soup):
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if ".onion" in href:
            links.add(href.split("#")[0])

    return links


def save_new_urls(path: str, urls: set):
    try:
        with open(path, "r", encoding="utf-8") as f:
            existing = set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        existing = set()

    new_urls = urls - existing

    if not new_urls:
        return 0

    with open(path, "a", encoding="utf-8") as f:
        for u in sorted(new_urls):
            f.write(u + "\n")

    return len(new_urls)
