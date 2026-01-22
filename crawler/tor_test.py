import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils.logger import log
from utils.analyzer import analyze_keywords, classify_severity
from utils.parser import parse_title, extract_text, classify_site_by_title
from utils.scorer import calculate_risk_score

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

with open("data/urls.txt", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

def main():
    print("crawler started")

    for url in urls:
        print(f"TRY {url}")
        time = datetime.now().isoformat()

        try:
            r = requests.get(url, proxies=proxies, timeout=30)
            r.encoding = "utf-8"

            soup = BeautifulSoup(r.text, "lxml")

            title = parse_title(r.text)
            site_type = classify_site_by_title(title)

            hits = analyze_keywords(text)
            severity = classify_severity(hits)

            risk_score = calculate_risk_score(severity, site_type, hits)

            print(f"RESULT url={url} | type={site_type} | severity={severity} | score={risk_score}")
            log("logs/run.log", {
                "time": time,
                "url": url,
                "title": title,
                "severity": severity,
                "site_type" : site_type,
                "hits": hits,
                "risk_score" : risk_score
            })

        except Exception as e:
            log("logs/error.log", {
                "time": time,
                "url": url,
                "error": str(e)
            })

if __name__ == "__main__":
    main()
