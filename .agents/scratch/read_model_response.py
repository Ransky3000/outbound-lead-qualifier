import os
import json

log_path = r"C:\Users\USER\.gemini\antigravity\brain\5b991568-455d-46b9-9bf0-f47f4d719a39\.system_generated\logs\overview.txt"
if os.path.exists(log_path):
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines):
        if '"source":"USER' in line:
            try:
                data = json.loads(line)
                print(f"Line {i} | Source: {data.get('source')} | Content: {data.get('content')}")
            except Exception:
                print(f"Line {i} | Raw: {line[:200]}")
else:
    print("Log file not found.")
