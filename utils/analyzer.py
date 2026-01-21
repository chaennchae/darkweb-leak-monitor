KEYWORDS = {
    "critical": ["database dump", "data breach", "leak database"],
    "credential": ["password", "credential", "login", "account"],
    "pii": ["email", "phone", "ssn"]
}

def analyze_keywords(text: str):
    hits = {k: [] for k in KEYWORDS}

    for level, words in KEYWORDS.item():
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
    return "NONE"