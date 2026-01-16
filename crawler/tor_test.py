import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

url = "http://check.torproject.org"

try:
    r = requests.get(url, proxies=proxies, timeout=30)
    print(r.text[:500])
except Exception as e:
    print("Error", e)