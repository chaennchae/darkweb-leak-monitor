def calculate_lisk_score(severity, site_type, hits):
    score = 0

    if severity == "HIGH":
        score += 50
    elif severity == "MEDIUM":
        score += 30
    elif severity == "LOW":
        score += 10

    score += len(hits["critical"]) * 15
    score += len(hits["credential"]) * 10
    score += len(hits["pii"]) * 5

    if site_type == "LEAK_SITE":
        score += 20
    elif site_type == "RANSOMEWARE":
        score += 25
    elif site_type == "MARKET":
        score += 10
    elif site_type == "FORUM":
        score += 5
    
    return score