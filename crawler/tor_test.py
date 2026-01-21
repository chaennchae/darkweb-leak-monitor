import requests
from datetime import datetime
from utils.logger import log
from utils.analyzer import analyze_keywords, classify_severity


# TODO: HTML 파싱 기반 키워드 탐지 (BeautifulSoup)

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}


with open("data/urls.txt", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]


def main():   
    print("[*] crawler started")
    for url in urls:
        print(f"[TRY] {url}")
        time = datetime.now().isoformat()

        try:
            r = requests.get(url, proxies=proxies, timeout=30)
            text = r.text.lower()

            hits = analyze_keywords(text)
            severity = classify_severity(hits)

            print(f"[RESULT] {url} severity={severity}")

            log("log/run.log", {
                "time": time,
                "url": url,
                "severity": severity,
                "hit": hits
            })

        except Exception as e:
            log("logs/error.log", {
                "time": time,
                "url": url,
                "error": str(e)
            })

if __name__ == "__main__":
    main()
