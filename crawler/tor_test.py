import traceback
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from utils.logger import log
from utils.analyzer import analyze_keywords, classify_severity
from utils.parser import parse_title, extract_text, classify_site_by_title
from utils.scorer import calculate_risk_score as get_score
from utils.notifier import send_alert
from utils.discovery import extract_onion_links, save_new_urls

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

with open("data/urls.txt", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

def main():
    print("crawler started")

    session = requests.Session()
    session.proxies.update(proxies)
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    })

    for url in urls:
        print(f"\n[*] TRY {url} ...", end="", flush=True)
        timestamp = datetime.now().isoformat()

        try:
            r = session.get(url, timeout=(15, 60))
            r.encoding = "utf-8"

            print(f"DONE (Status: {r.status_code})")

            soup = BeautifulSoup(r.text, "lxml")
            
            new_links = extract_onion_links(soup)

            print(f"[DEBUG] extracted {len(new_links)} onion links")
            added = save_new_urls("data/urls.txt", new_links)

            if added:
                print(f"[+] discoverd {added} new onion urls")

            title = parse_title(soup)
            site_type = classify_site_by_title(title)
            text = extract_text(r.text)

            hits = analyze_keywords(text)
            severity = classify_severity(hits)
            print(f"DEBUG: type of calculate_risk_score is {type(get_score)}")
            risk_score = get_score(severity, site_type, hits)


            if risk_score >= 60:
                msg = (
                    f"[ALERT]\n"
                    f"URL: {url}\n"
                    f"Title: {title}\n"
                    f"Type: {site_type}\n"
                    f"Severity: {severity}\n"
                    f"Score: {risk_score}\n"
                    f"Hits: {hits}"
                )

                send_alert(msg)

            print(
                f"RESULT url={url} | "
                f"type={site_type} | "
                f"severity={severity} | "
                f"score={risk_score}"
            )

            print(f"RESULT url={url} | type={site_type} | severity={severity} | score={risk_score}")
            log("logs/run.log", {
                "time": timestamp,
                "url": url,
                "title": title,
                "severity": severity,
                "site_type" : site_type,
                "hits": hits,
                "risk_score" : risk_score
            })

        except requests.exceptions.RequestException as e:
            #network관련 에러 처리
            print(f" FAILED ({type(e).__name__})")
            log("logs/error.log", {"time": timestamp, "url": url, "error": str(e)})
        
        except Exception as e:
            print(f" ERROR: ")
            print(traceback.format_exc())
            #log("logs/error.log", {"time": timestamp, "url": url, "error": str(e)})

if __name__ == "__main__":
    main()
