from bs4 import BeautifulSoup

def parse_title(soup):
    """BeautifulSoup 객체에서 제목 추출"""
    if not hasattr(soup, "title"):
        return "No Title"
        
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "No Title"

def extract_text(soup_or_html):
    """HTML 문자열이나 soup 객체에서 텍스트만 추출 (에러 방지 로직 포함)"""
    if isinstance(soup_or_html, str):
        soup = BeautifulSoup(soup_or_html, "lxml")
    else:
        soup = soup_or_html

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split()).lower()

def classify_site_by_title(title: str):
    """site title"""
    if not title or not isinstance(title, str):
        return "UNKNOWN"
    
    t = title.lower()

    if any(x in t for x in ["leak", "breach", "dump"]):
        return "LEAK_SITE"
    if any(x in t for x in ["ransom", "locker", "lockbit"]):
        return "RANSOMWARE" 
    if any(x in t for x in ["forum", "board"]):
        return "FORUM"
    if any(x in t for x in ["market", "shop"]):
        return "MARKET"
    
    return "OTHER"