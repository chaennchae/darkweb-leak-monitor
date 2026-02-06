import os

def load_urls(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

def save_url(path, url):
    with open(path, "a", encoding="utf-8") as f:
        f.write(url + "\n")

def push_new_urls(frontier_path, visited, new_urls):
    added = 0
    for u in new_urls:
        if u not in visited:
            save_url(frontier_path, u)
            added += 1
    return added
