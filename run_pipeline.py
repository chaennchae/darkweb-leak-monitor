import os

print("[*] Starting darkweb pipeline...")

print("[*] Running crawler...")
os.system("python -m crawler.tor_test")

print("[*] Generating report...")
os.system("python -m report.generator")

print("[*] Done.")
