import json
from datetime import datetime
from collections import Counter
from pathlib import Path

LOG_FILE = "logs/run.log"
REPORT_DIR = "reports"


def load_logs():
    records = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                records.append(json.loads(line))
            except:
                continue
    return records


def severity_color(sev):
    colors = {
        "HIGH": "#ff4d4d",
        "MEDIUM": "#ffa500",
        "LOW": "#4da6ff",
        "NONE": "#999999"
    }
    return colors.get(sev, "#000000")


def generate_report():
    records = load_logs()

    if not records:
        print("No records found.")
        return

    total = len(records)
    avg_score = sum(r["risk_score"] for r in records) / total

    site_types = Counter(r["site_type"] for r in records)
    severities = Counter(r["severity"] for r in records)

    # 🔝 Top 10 by risk score
    top10 = sorted(records, key=lambda x: x["risk_score"], reverse=True)[:10]

    today = datetime.now().strftime("%Y-%m-%d")
    Path(REPORT_DIR).mkdir(exist_ok=True)
    report_path = f"{REPORT_DIR}/{today}.html"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"""
<html>
<head>
<title>Darkweb Intelligence Report {today}</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background-color: #111;
    color: #eee;
    margin: 40px;
}}
h1, h2 {{
    color: #00ffcc;
}}
table {{
    width: 100%;
    border-collapse: collapse;
}}
th, td {{
    padding: 10px;
    border-bottom: 1px solid #333;
    text-align: left;
}}
th {{
    background-color: #222;
}}
tr:hover {{
    background-color: #1a1a1a;
}}
.high-risk {{
    font-weight: bold;
}}
</style>
</head>
<body>

<h1>Darkweb Intelligence Report</h1>
<p><strong>Date:</strong> {today}</p>

<h2>Summary</h2>
<p>Total Crawled: {total}</p>
<p>Average Risk Score: {avg_score:.2f}</p>

<h2>Severity Distribution</h2>
<pre>{dict(severities)}</pre>

<h2>Site Type Distribution</h2>
<pre>{dict(site_types)}</pre>

<h2>Top 10 Risk Sites</h2>

<table>
<tr>
<th>Rank</th>
<th>URL</th>
<th>Risk Score</th>
<th>Severity</th>
<th>Type</th>
</tr>
""")

        for idx, r in enumerate(top10, start=1):
            color = severity_color(r["severity"])
            high_class = "high-risk" if r["risk_score"] >= 60 else ""
            f.write(f"""
<tr class="{high_class}">
<td>{idx}</td>
<td>{r['url']}</td>
<td>{r['risk_score']}</td>
<td style="color:{color}">{r['severity']}</td>
<td>{r['site_type']}</td>
</tr>
""")

        f.write("""
</table>

</body>
</html>
""")

    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    generate_report()
