from bs4 import BeautifulSoup

def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    #의미없는 태그 제거
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    #사람이 읽는 txt만 추출
    text = soup.get_text(separator=" ")

    #공백 정리
    text = " ".join(text.split())

    return text.lower()
