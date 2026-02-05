from bs4 import BeautifulSoup

def parse_title(soup):
    """BeautifulSoup 객체에서 제목 추출"""
    # soup이 BeautifulSoup 객체인지 확인 (안전장치)
    if not hasattr(soup, "title"):
        return "No Title"
        
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "No Title"

def extract_text(soup_or_html):
    """HTML 문자열이나 soup 객체에서 텍스트만 추출 (에러 방지 로직 포함)"""
    # 1. 입력값이 문자열이면 BeautifulSoup 객체로 변환 (TypeError: 'str' object is not callable 방지)
    if isinstance(soup_or_html, str):
        soup = BeautifulSoup(soup_or_html, "lxml")
    else:
        soup = soup_or_html

    # 2. 불필요한 태그 제거
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # 3. 텍스트 추출 및 공백 정규화
    text = soup.get_text(separator=" ")
    return " ".join(text.split()).lower()

def classify_site_by_title(title: str):
    """사이트 제목 기반 유형 분류"""
    if not title or not isinstance(title, str):
        return "UNKNOWN"
    
    t = title.lower()

    if any(x in t for x in ["leak", "breach", "dump"]):
        return "LEAK_SITE"
    if any(x in t for x in ["ransom", "locker", "lockbit"]):
        return "RANSOMWARE"  # 오타 수정 (RANSOMEWARE -> RANSOMWARE)
    if any(x in t for x in ["forum", "board"]):
        return "FORUM"
    if any(x in t for x in ["market", "shop"]):
        return "MARKET"
    
    return "OTHER"