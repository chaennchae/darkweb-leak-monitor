import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

url = url = "http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"


r = requests.get(url, proxies=proxies, timeout=120)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, "lxml")

# 페이지 제목
title = soup.title.text if soup.title else "No title"
print("TITLE: ", title)

# 모든 링크
links = soup.find_all("a")
print(f"Found {len(links)} links")

for link in links[:5]:
    print("-", link.get_text(strip=True), "->", link.get("href"))