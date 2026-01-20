import requests
import json
from datetime import datetime

# TODO: HTML 파싱 기반 키워드 탐지 (BeautifulSoup)

def log(filename, msg):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

KEYWORDS = {
    "critical": ["database dump", "data breach", "leak database"],
    "credential": ["password", "credential", "login", "account"],
    "pii": ["email", "phone", "ssn"]
}

with open("../data/urls.txt") as f:
    urls = [line.strip() for line in f if line.strip()]

def analyze_keywords(text):
    hits = {
        "critical": [],
        "credential": [],
        "pii": []
    }

    for level, words in KEYWORDS.items():
        for w in words:
            if w in text:
                hits[level].append(w)

    return hits

def classify_severity(hits):
    if hits["critical"]:
        return "HIGH"
    elif hits["credential"] and hits["pii"]:
        return "MEDIUM"
    elif hits["credential"] or hits["pii"]:
        return "LOW"
    else:
        return "NONE"
    
for url in urls:
    time = datetime.now().isoformat()

    try:
        r = requests.get(url, proxies=proxies, timeout=30)
        text = r.text.lower()

        hits = analyze_keywords(text)
        severity = classify_severity(hits)

        if severity != "NONE":
            log_data = {
                "time": time,
                "url": url,
                "severity": severity,
                "hits": hits
            }

            log("../logs/found.log", json.dumps(log_data, ensure_ascii=False))

    except Exception as e:
        error_data = {
            "time": time,
            "url": url,
            "error": str(e)
        }
        log("../logs/error.log", json.dumps(error_data, ensure_ascii=False))
