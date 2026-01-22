from bs4 import BeautifulSoup

def parse_title(soup):
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return None

def extract_text(soup):
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split()).lower()

def classify_site_by_title(title: str):
    if not title:
        return "UNKNOWN"
    
    t = title.lower()

    if any(x in t for x in ["leak", "breach", "dump"]):
        return "LEAK_SITE"
    if any(x in t for x in ["ransom", "locker", "lockbit"]):
        return "RANSOMEWARE"
    if any(x in t for x in ["forum", "board"]):
        return "FORUM"
    if any(x in t for x in ["market", "shop"]):
        return "MARKET"
    
    return "OTHER"